import streamlit as st
import datetime
import random
import time

# ─── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Algérie Télécom — App Client Hybride",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;700&family=Space+Mono:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #003DA5 0%, #00235A 100%);
    color: white;
}
section[data-testid="stSidebar"] * {color: white !important;}
section[data-testid="stSidebar"] .stRadio label {
    font-size: 15px;
    padding: 6px 0;
}

/* ── Main background ── */
.main { background: #F4F7FF; }

/* ── Card style ── */
.card {
    background: white;
    border-radius: 14px;
    padding: 24px;
    margin-bottom: 18px;
    box-shadow: 0 2px 12px rgba(0,61,165,0.08);
    border: 1px solid #E0E8FF;
}

/* ── Metric card ── */
.metric-card {
    background: linear-gradient(135deg, #003DA5 0%, #0057E7 100%);
    border-radius: 14px;
    padding: 20px 24px;
    color: white;
    text-align: center;
    box-shadow: 0 4px 16px rgba(0,61,165,0.25);
}
.metric-card .value {
    font-family: 'Space Mono', monospace;
    font-size: 2.2rem;
    font-weight: 700;
    margin: 6px 0;
}
.metric-card .label {font-size: 13px; opacity: 0.85;}

/* ── Status badges ── */
.badge {
    display: inline-block;
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    margin-right: 6px;
}
.badge-green  {background:#DCFCE7; color:#16A34A;}
.badge-orange {background:#FEF3C7; color:#D97706;}
.badge-blue   {background:#DBEAFE; color:#1D4ED8;}
.badge-red    {background:#FEE2E2; color:#DC2626;}

/* ── Chat bubbles ── */
.bubble-user {
    background: #003DA5;
    color: white;
    border-radius: 18px 18px 4px 18px;
    padding: 10px 16px;
    margin: 6px 0 6px 80px;
    font-size: 14px;
}
.bubble-bot {
    background: white;
    color: #1E293B;
    border-radius: 18px 18px 18px 4px;
    padding: 10px 16px;
    margin: 6px 80px 6px 0;
    font-size: 14px;
    border: 1px solid #E0E8FF;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.bubble-agent {
    background: #F0FFF4;
    color: #14532D;
    border-radius: 18px 18px 18px 4px;
    padding: 10px 16px;
    margin: 6px 80px 6px 0;
    font-size: 14px;
    border: 1px solid #BBF7D0;
}

/* ── Section headers ── */
.section-title {
    font-family: 'Space Mono', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    color: #003DA5;
    letter-spacing: -0.3px;
    margin-bottom: 4px;
}
.section-sub {
    font-size: 13px;
    color: #64748B;
    margin-bottom: 18px;
}

/* ── Star rating ── */
.stars { font-size: 1.8rem; }

/* ── Timeline ── */
.timeline-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px dashed #E2E8F0;
}
.timeline-dot {
    width: 12px; height: 12px;
    border-radius: 50%;
    margin-top: 4px;
    flex-shrink: 0;
}
.dot-green  {background:#22C55E;}
.dot-orange {background:#F59E0B;}
.dot-blue   {background:#3B82F6;}
.dot-gray   {background:#CBD5E1;}

/* ── Progress bar override ── */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #003DA5, #0057E7);
}

/* ── Expander ── */
details summary {font-weight: 600; color: #003DA5;}

/* ── Button override ── */
.stButton > button {
    background: linear-gradient(135deg, #003DA5, #0057E7);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 8px 20px;
    font-weight: 600;
    font-family: 'DM Sans', sans-serif;
    transition: opacity .2s;
}
.stButton > button:hover {opacity: 0.88;}

/* ── Alert-style info box ── */
.info-box {
    background: #EFF6FF;
    border-left: 4px solid #003DA5;
    border-radius: 0 8px 8px 0;
    padding: 12px 16px;
    font-size: 14px;
    color: #1E3A8A;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# ─── Session state init ─────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "bot", "text": "👋 Bonjour ! Je suis l'assistant virtuel d'Algérie Télécom. Comment puis-je vous aider ?"}
    ]
if "escalated" not in st.session_state:
    st.session_state.escalated = False
if "claims" not in st.session_state:
    st.session_state.claims = [
        {"id": "REC-2024-001", "type": "Panne Internet", "date": "12/05/2024", "status": "Résolu",     "progress": 100},
        {"id": "REC-2024-002", "type": "Facture erronée","date": "20/05/2024", "status": "En cours",   "progress": 60},
        {"id": "REC-2024-003", "type": "Lenteur réseau",  "date": "22/05/2024", "status": "En attente","progress": 20},
    ]
if "csat_done" not in st.session_state:
    st.session_state.csat_done = False
if "nps_done" not in st.session_state:
    st.session_state.nps_done = False
if "simplified" not in st.session_state:
    st.session_state.simplified = False

# ─── Chatbot logic ──────────────────────────────────────────────────────────────
FAQ = {
    "horaire": "🕐 Nos agences sont ouvertes du dimanche au jeudi, de 8h00 à 17h00.",
    "facture": "💳 Votre dernière facture est disponible dans l'onglet **Tableau de bord**. Montant : **4 200 DA** — échéance le 30/05/2024.",
    "panne":   "🔧 Vous pouvez signaler une panne directement depuis l'onglet **Signalement**. Un technicien vous contactera sous 2h.",
    "offre":   "📦 Nos offres Fibre : Starter 100 Mb/s à 2 500 DA/mois, Plus 300 Mb/s à 4 200 DA/mois, Pro 1 Gb/s à 7 500 DA/mois.",
    "résiliation": "📝 Pour résilier, rendez-vous en agence avec votre CIN et votre contrat. Un préavis de 30 jours est requis.",
    "débit":   "📶 Testez votre débit sur fast.com. Si le problème persiste, signalez une panne dans l'onglet dédié.",
    "contact": "📞 Notre service client est joignable au **3023** (24h/7j) ou par email à **support@algerietelecom.dz**.",
}

def chatbot_response(user_msg: str) -> tuple[str, bool]:
    msg = user_msg.lower()
    for kw, answer in FAQ.items():
        if kw in msg:
            return answer, False
    if any(w in msg for w in ["agent", "humain", "personne", "conseiller", "parler"]):
        return "🔄 Je vous transfère vers un agent humain. Veuillez patienter...", True
    return ("Je n'ai pas bien compris votre demande. Voici ce que je peux vous aider avec : "
            "**horaires**, **facture**, **panne**, **offres**, **débit**, **contact**.\n\n"
            "Tapez **agent** pour parler à un conseiller humain.", False), False

# ─── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📡 Algérie Télécom")
    st.markdown("**Application Client Hybride**")
    st.markdown("---")

    # Mode simplifié toggle
    simplified = st.toggle("🧓 Mode simplifié (seniors)", value=st.session_state.simplified)
    st.session_state.simplified = simplified
    st.markdown("---")

    page = st.radio("Navigation", [
        "🏠 Accueil",
        "💬 Service Client (Chatbot)",
        "🔧 Signalement de panne",
        "📋 Suivi des réclamations",
        "⭐ Satisfaction (CSAT / NPS)",
        "📚 Guide numérique",
        "📊 Tableau de bord",
    ])
    st.markdown("---")
    st.markdown("**Client :** Mohamed Amrani")
    st.markdown("**Contrat :** Fibre Pro · 1 Gb/s")
    st.markdown('<span class="badge badge-green">Actif</span>', unsafe_allow_html=True)
    st.markdown("---")
    st.caption("v1.0 · Prototype — Mémoire 2024")

# ─── Font size for simplified mode ─────────────────────────────────────────────
if st.session_state.simplified:
    st.markdown("<style>body, p, li, label {font-size: 18px !important;}</style>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: ACCUEIL
# ══════════════════════════════════════════════════════════════════════════════
if page == "🏠 Accueil":
    st.markdown("# Bienvenue, Mohamed 👋")
    st.markdown("#### Votre espace client Algérie Télécom — Application Hybride")
    st.markdown("---")

    # KPI cards
    col1, col2, col3, col4 = st.columns(4)
    kpis = [
        ("98.7%", "Disponibilité réseau"),
        ("1m 42s", "Temps moyen de réponse"),
        ("4.3/5", "Score CSAT actuel"),
        ("72", "NPS (Net Promoter Score)"),
    ]
    for col, (val, lbl) in zip([col1, col2, col3, col4], kpis):
        col.markdown(f"""
        <div class="metric-card">
            <div class="label">{lbl}</div>
            <div class="value">{val}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📣 Dernières notifications</div>', unsafe_allow_html=True)
        notifications = [
            ("🟢", "22/05", "Votre réclamation REC-2024-001 a été résolue."),
            ("🟡", "21/05", "Maintenance programmée le 25/05 de 2h à 4h."),
            ("🔵", "20/05", "Nouvelle facture disponible — 4 200 DA."),
        ]
        for icon, date, msg in notifications:
            st.markdown(f"{icon} **{date}** — {msg}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">⚡ Accès rapide</div>', unsafe_allow_html=True)
        st.markdown("Utilisez la **barre de navigation** à gauche pour accéder aux modules :")
        items = [
            ("💬", "Chatbot + escalade vers un agent humain"),
            ("🔧", "Signaler une panne avec photo/géoloc"),
            ("📋", "Suivre vos réclamations en temps réel"),
            ("⭐", "Donner votre avis après chaque interaction"),
            ("📚", "Tutoriels pour les non-initiés"),
            ("📊", "Consulter votre tableau de bord"),
        ]
        for icon, label in items:
            st.markdown(f"{icon} {label}")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-box">💡 <b>Mode hors ligne disponible :</b> Les informations de votre dernier accès restent consultables sans connexion.</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: CHATBOT
# ══════════════════════════════════════════════════════════════════════════════
elif page == "💬 Service Client (Chatbot)":
    st.markdown("# 💬 Service Client")
    st.markdown('<div class="section-sub">Chatbot disponible 24h/7j · Escalade vers un agent humain si besoin</div>', unsafe_allow_html=True)

    # Display conversation
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f'<div class="bubble-user">{msg["text"]}</div>', unsafe_allow_html=True)
            elif msg["role"] == "bot":
                st.markdown(f'<div class="bubble-bot">🤖 {msg["text"]}</div>', unsafe_allow_html=True)
            elif msg["role"] == "agent":
                st.markdown(f'<div class="bubble-agent">👨‍💼 <b>Agent Karim :</b> {msg["text"]}</div>', unsafe_allow_html=True)

    st.markdown("---")

    if st.session_state.escalated:
        st.success("👨‍💼 **Agent Karim** est connecté et prend en charge votre demande.")
        agent_input = st.text_input("Votre message à l'agent :", key="agent_msg", placeholder="Écrivez votre message...")
        if st.button("📤 Envoyer à l'agent") and agent_input:
            st.session_state.chat_history.append({"role": "user",  "text": agent_input})
            st.session_state.chat_history.append({"role": "agent", "text": "Merci pour votre message. Je vérifie votre dossier immédiatement. Pouvez-vous me confirmer votre numéro de contrat ?"})
            st.rerun()
        if st.button("❌ Terminer la conversation"):
            st.session_state.escalated = False
            st.session_state.chat_history.append({"role": "bot", "text": "La conversation avec l'agent est terminée. N'hésitez pas à nous recontacter. 😊"})
            st.rerun()
    else:
        # Quick suggestion buttons
        st.markdown("**Suggestions rapides :**")
        cols = st.columns(4)
        suggestions = ["Mes horaires d'agence", "Ma facture", "Signaler une panne", "Nos offres"]
        for i, sug in enumerate(suggestions):
            if cols[i].button(sug, key=f"sug_{i}"):
                st.session_state.chat_history.append({"role": "user", "text": sug})
                resp, esc = chatbot_response(sug)
                if isinstance(resp, tuple): resp = resp[0]
                st.session_state.chat_history.append({"role": "bot", "text": resp})
                if esc:
                    st.session_state.escalated = True
                st.rerun()

        user_input = st.text_input("Votre message :", key="user_msg", placeholder="Posez votre question ici...")
        col_send, col_agent = st.columns([2, 1])
        with col_send:
            if st.button("📤 Envoyer") and user_input:
                st.session_state.chat_history.append({"role": "user", "text": user_input})
                resp, esc = chatbot_response(user_input)
                if isinstance(resp, tuple): resp = resp[0]
                st.session_state.chat_history.append({"role": "bot", "text": resp})
                if esc:
                    st.session_state.escalated = True
                st.rerun()
        with col_agent:
            if st.button("👨‍💼 Parler à un agent"):
                st.session_state.chat_history.append({"role": "user", "text": "Je souhaite parler à un agent humain."})
                st.session_state.chat_history.append({"role": "bot", "text": "🔄 Transfert en cours... Un agent vous rejoint dans quelques instants."})
                st.session_state.escalated = True
                st.rerun()

    st.markdown('<div class="info-box">📊 <b>KPI :</b> Taux de résolution chatbot cible : <b>70%</b> · Taux d\'escalade cible : <b>&lt; 30%</b> · Temps de réponse agent cible : <b>&lt; 2 min</b></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: SIGNALEMENT
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🔧 Signalement de panne":
    st.markdown("# 🔧 Signalement de panne")
    st.markdown('<div class="section-sub">Photo + géolocalisation · Traitement prioritaire</div>', unsafe_allow_html=True)

    with st.form("form_panne"):
        col1, col2 = st.columns(2)
        with col1:
            panne_type = st.selectbox("Type de panne *", [
                "Panne Internet totale",
                "Lenteur / débit réduit",
                "Coupure téléphonique",
                "Problème TV / décodeur",
                "Autre",
            ])
            gravite = st.select_slider("Gravité", options=["Faible", "Moyenne", "Élevée", "Critique"], value="Moyenne")
        with col2:
            debut = st.date_input("Date de début *", datetime.date.today())
            heure = st.time_input("Heure approximative", datetime.time(8, 0))

        description = st.text_area("Description de la panne *", placeholder="Décrivez le problème en détail...", height=100)

        st.markdown("**📍 Géolocalisation**")
        col_lat, col_lon = st.columns(2)
        lat = col_lat.text_input("Latitude", "36.7372")
        lon = col_lon.text_input("Longitude", "3.0868")

        photo = st.file_uploader("📷 Photo de la panne (optionnel)", type=["jpg", "jpeg", "png"])
        if photo:
            st.image(photo, caption="Aperçu de la photo", width=250)

        submit = st.form_submit_button("📤 Soumettre le signalement")

    if submit:
        ref = f"REC-2024-{random.randint(100,999)}"
        st.success(f"✅ Signalement envoyé avec succès ! Référence : **{ref}**")
        st.markdown(f"""
        <div class="card">
            <div class="section-title">📋 Récapitulatif du signalement</div>
            <p>🔹 <b>Référence :</b> {ref}</p>
            <p>🔹 <b>Type :</b> {panne_type}</p>
            <p>🔹 <b>Gravité :</b> {gravite}</p>
            <p>🔹 <b>Date :</b> {debut} à {heure}</p>
            <p>🔹 <b>Géolocalisation :</b> {lat}, {lon}</p>
            <p>🔹 <b>Statut initial :</b> <span class="badge badge-orange">En attente</span></p>
            <p>⏱️ Un technicien vous contactera dans les <b>2 heures</b>.</p>
        </div>
        """, unsafe_allow_html=True)
        new_claim = {"id": ref, "type": panne_type, "date": str(debut), "status": "En attente", "progress": 10}
        st.session_state.claims.append(new_claim)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: SUIVI DES RÉCLAMATIONS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📋 Suivi des réclamations":
    st.markdown("# 📋 Suivi des réclamations")
    st.markdown('<div class="section-sub">Historique complet · Mise à jour en temps réel</div>', unsafe_allow_html=True)

    status_colors = {"Résolu": "badge-green", "En cours": "badge-orange", "En attente": "badge-blue"}
    status_dots   = {"Résolu": "dot-green",  "En cours": "dot-orange",  "En attente": "dot-gray"}

    for claim in reversed(st.session_state.claims):
        with st.expander(f"🗂️ {claim['id']} — {claim['type']}  |  {claim['date']}", expanded=(claim["status"] == "En cours")):
            col_s, col_p = st.columns([1, 2])
            with col_s:
                badge_cls = status_colors.get(claim["status"], "badge-blue")
                st.markdown(f'**Statut :** <span class="badge {badge_cls}">{claim["status"]}</span>', unsafe_allow_html=True)
                st.markdown(f"**Date :** {claim['date']}")
            with col_p:
                st.markdown(f"**Avancement : {claim['progress']}%**")
                st.progress(claim["progress"] / 100)

            # Timeline
            st.markdown("**Historique :**")
            timeline = [
                ("dot-blue",   "Signalement reçu et enregistré"),
                ("dot-orange", "Assigné à un technicien"),
                ("dot-orange" if claim["progress"] < 80 else "dot-green", "Diagnostic en cours"),
                ("dot-green"  if claim["progress"] == 100 else "dot-gray", "Résolution / Clôture"),
            ]
            for dot_cls, label in timeline:
                st.markdown(f"""
                <div class="timeline-item">
                    <div class="timeline-dot {dot_cls}"></div>
                    <div style="font-size:14px;">{label}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="info-box">🔔 <b>Notifications push</b> : Vous recevrez une alerte à chaque changement de statut sur votre réclamation.</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: SATISFACTION
# ══════════════════════════════════════════════════════════════════════════════
elif page == "⭐ Satisfaction (CSAT / NPS)":
    st.markdown("# ⭐ Satisfaction client")
    st.markdown('<div class="section-sub">CSAT après chaque interaction · NPS trimestriel · Boîte à idées</div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 CSAT — Satisfaction", "📈 NPS — Recommandation", "💡 Boîte à idées"])

    with tab1:
        if not st.session_state.csat_done:
            st.markdown("### Évaluez votre dernière interaction")
            st.markdown("*Suite à votre contact avec notre service client le 22/05/2024*")
            csat = st.radio("Comment évaluez-vous notre service ?", ["⭐ Très insatisfait", "⭐⭐ Insatisfait", "⭐⭐⭐ Neutre", "⭐⭐⭐⭐ Satisfait", "⭐⭐⭐⭐⭐ Très satisfait"], index=3)
            commentaire = st.text_area("Commentaire (optionnel)", placeholder="Que pourrions-nous améliorer ?")
            categories = st.multiselect("Points à améliorer", ["Temps d'attente", "Compétence du conseiller", "Clarté des explications", "Résolution du problème", "Suivi post-interaction"])
            if st.button("✅ Soumettre mon avis CSAT"):
                st.session_state.csat_done = True
                st.rerun()
        else:
            st.success("✅ Merci pour votre évaluation CSAT ! Votre retour nous aide à améliorer nos services.")
            st.markdown("**Résultats globaux CSAT (derniers 30 jours) :**")
            csat_data = {"⭐": 3, "⭐⭐": 8, "⭐⭐⭐": 17, "⭐⭐⭐⭐": 35, "⭐⭐⭐⭐⭐": 37}
            for stars, pct in csat_data.items():
                col_s, col_b = st.columns([1, 4])
                col_s.write(stars)
                col_b.progress(pct / 100)

    with tab2:
        if not st.session_state.nps_done:
            st.markdown("### Enquête NPS trimestrielle")
            st.markdown("*Recommanderiez-vous Algérie Télécom à votre entourage ?*")
            nps = st.slider("Note de 0 (pas du tout) à 10 (certainement)", 0, 10, 7)
            if nps <= 6:
                st.warning("😞 Vous êtes **Détracteur** — Votre avis est précieux pour nous améliorer.")
            elif nps <= 8:
                st.info("😐 Vous êtes **Passif** — Merci de votre confiance.")
            else:
                st.success("😊 Vous êtes **Promoteur** — Merci pour votre fidélité !")
            raison = st.text_area("Pourquoi cette note ?", placeholder="Expliquez votre choix...")
            if st.button("✅ Soumettre mon NPS"):
                st.session_state.nps_done = True
                st.rerun()
        else:
            st.success("✅ Merci pour votre participation à l'enquête NPS !")
            st.markdown("**NPS global Algérie Télécom :** `72` — Excellent")
            col1, col2, col3 = st.columns(3)
            col1.metric("Promoteurs", "68%",  "+5%")
            col2.metric("Passifs",    "20%",  "-2%")
            col3.metric("Détracteurs","12%",  "-3%")

    with tab3:
        st.markdown("### 💡 Boîte à idées")
        st.markdown("*Vos suggestions contribuent directement à l'amélioration de nos services (co-création)*")
        categorie_idee = st.selectbox("Catégorie", ["Application mobile", "Service client", "Offres et tarifs", "Réseau et couverture", "Accessibilité", "Autre"])
        titre_idee = st.text_input("Titre de votre idée")
        desc_idee  = st.text_area("Description détaillée", height=120)
        if st.button("💡 Soumettre mon idée"):
            if titre_idee and desc_idee:
                st.success(f"✅ Idée **'{titre_idee}'** soumise avec succès ! Elle sera analysée par notre équipe Innovation.")
            else:
                st.warning("Veuillez remplir le titre et la description.")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: GUIDE NUMÉRIQUE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📚 Guide numérique":
    st.markdown("# 📚 Espace d'inclusion numérique")
    st.markdown('<div class="section-sub">Tutoriels simples · Accessible aux seniors et zones rurales · Mode simplifié disponible</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-box">🧓 Ce module répond à la <b>fracture numérique</b> identifiée dans le mémoire (§3.1.7) : 30 à 40% de la population manque de compétences numériques.</div>', unsafe_allow_html=True)

    tutorials = {
        "📶 Comment vérifier mon débit Internet ?": [
            "1️⃣ Ouvrez votre navigateur (ex: Chrome, Firefox).",
            "2️⃣ Tapez **fast.com** dans la barre d'adresse.",
            "3️⃣ Le test démarre automatiquement.",
            "4️⃣ Un débit normal est supérieur à **50 Mb/s** pour la Fibre.",
            "5️⃣ Si votre débit est trop faible, signalez une panne dans l'application.",
        ],
        "📄 Comment lire ma facture ?": [
            "1️⃣ Ouvrez l'onglet **Tableau de bord**.",
            "2️⃣ Cliquez sur **Mes factures**.",
            "3️⃣ La date d'échéance est affichée en rouge si dépassée.",
            "4️⃣ Vous pouvez payer en ligne ou en agence.",
            "5️⃣ Conservez vos factures au moins 12 mois.",
        ],
        "🔒 Comment sécuriser ma box WiFi ?": [
            "1️⃣ Connectez-vous à **192.168.1.1** depuis votre navigateur.",
            "2️⃣ Identifiant par défaut : **admin** / Mot de passe : **admin**.",
            "3️⃣ Changez immédiatement le mot de passe WiFi.",
            "4️⃣ Choisissez un mot de passe d'au moins 12 caractères.",
            "5️⃣ Ne partagez votre WiFi qu'avec des personnes de confiance.",
        ],
        "📞 Comment contacter le service client ?": [
            "1️⃣ **Par téléphone :** composez le **3023** (disponible 24h/7j).",
            "2️⃣ **Par chat :** utilisez l'onglet Service Client dans cette application.",
            "3️⃣ **En agence :** munissez-vous de votre CIN et numéro de contrat.",
            "4️⃣ **Par email :** support@algerietelecom.dz (réponse sous 24h).",
        ],
    }

    for title, steps in tutorials.items():
        with st.expander(title):
            for step in steps:
                st.markdown(f"{'<span style=font-size:18px>' if st.session_state.simplified else ''}{step}{'</span>' if st.session_state.simplified else ''}", unsafe_allow_html=True)
            st.markdown("---")
            st.markdown("📹 *Vidéo tutoriel disponible en agence ou sur notre chaîne YouTube.*")

    st.markdown("---")
    st.markdown("### ❓ Vous avez une question ?")
    question = st.text_input("Posez votre question en langage simple :", placeholder="Ex: Comment éteindre et rallumer ma box ?")
    if st.button("🔍 Chercher"):
        if question:
            st.info(f"💡 Pour la question **'{question}'** : Notre équipe prépare la réponse. En attendant, appelez le **3023** ou visitez une agence proche de chez vous.")

# ══════════════════════════════════════════════════════════════════════════════
# PAGE: TABLEAU DE BORD
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📊 Tableau de bord":
    st.markdown("# 📊 Tableau de bord personnel")
    st.markdown('<div class="section-sub">Consommation · Factures · Historique · Transparence totale</div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📡 Ma consommation", "💳 Mes factures", "📈 Statistiques KPI"])

    with tab1:
        st.markdown("### Consommation — Mai 2024")
        col1, col2, col3 = st.columns(3)
        col1.metric("Données utilisées", "342 Go",  "+12 Go vs avril")
        col2.metric("Appels effectués", "47 min",   "-8 min vs avril")
        col3.metric("SMS envoyés",       "12",       "=")

        st.markdown("**Utilisation des données (Go/semaine) :**")
        weeks = ["S1 (1-7 mai)", "S2 (8-14 mai)", "S3 (15-21 mai)", "S4 (22-31 mai — partiel)"]
        usage = [87, 95, 102, 58]
        for w, u in zip(weeks, usage):
            col_w, col_bar = st.columns([1, 3])
            col_w.write(w)
            col_bar.progress(u / 120)
            col_bar.caption(f"{u} Go")

    with tab2:
        st.markdown("### Historique des factures")
        factures = [
            ("Mai 2024",   "4 200 DA", "30/05/2024", "À payer"),
            ("Avril 2024", "4 200 DA", "30/04/2024", "Payée"),
            ("Mars 2024",  "4 200 DA", "30/03/2024", "Payée"),
            ("Fév. 2024",  "4 200 DA", "29/02/2024", "Payée"),
        ]
        for mois, montant, echeance, statut in factures:
            badge_cls = "badge-orange" if statut == "À payer" else "badge-green"
            col_m, col_mo, col_e, col_s, col_dl = st.columns([2, 1.5, 1.5, 1.5, 1])
            col_m.write(f"**{mois}**")
            col_mo.write(montant)
            col_e.write(echeance)
            col_s.markdown(f'<span class="badge {badge_cls}">{statut}</span>', unsafe_allow_html=True)
            col_dl.button("⬇️", key=f"dl_{mois}", help="Télécharger la facture PDF")
        st.markdown("---")
        if st.button("💳 Payer ma facture de Mai 2024"):
            with st.spinner("Redirection vers le portail de paiement sécurisé..."):
                time.sleep(1.5)
            st.success("✅ Redirection vers le portail de paiement — CIB / Dahabia / Virement.")

    with tab3:
        st.markdown("### Indicateurs de performance (KPI) — Tableau de bord opérationnel")
        st.markdown("*Extrait des KPI définis dans le mémoire de recherche*")

        kpi_data = [
            ("Taux de résolution chatbot",      "70%",  "68%",  "badge-orange"),
            ("Temps moyen de réponse agent",    "< 2 min", "1m42s", "badge-green"),
            ("Taux d'escalade humain",          "< 30%","24%",  "badge-green"),
            ("Score CSAT moyen",                "> 4/5","4.3/5","badge-green"),
            ("Taux d'adoption seniors",         "> 40%","31%",  "badge-orange"),
        ]
        header = st.columns([3, 1.5, 1.5, 1.5])
        header[0].markdown("**Indicateur**")
        header[1].markdown("**Cible**")
        header[2].markdown("**Actuel**")
        header[3].markdown("**Statut**")
        st.markdown("---")
        for name, cible, actuel, badge_cls in kpi_data:
            cols = st.columns([3, 1.5, 1.5, 1.5])
            cols[0].write(name)
            cols[1].write(cible)
            cols[2].write(f"**{actuel}**")
            cols[3].markdown(f'<span class="badge {badge_cls}">{"✅ OK" if badge_cls == "badge-green" else "⚠️ À améliorer"}</span>', unsafe_allow_html=True)

# ─── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<div style="text-align:center; font-size:12px; color:#94A3B8;">'
    '📡 Algérie Télécom · Application Client Hybride (PWA) · Prototype Streamlit · Mémoire 2024'
    '</div>',
    unsafe_allow_html=True
)
