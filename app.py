"""
Algérie Télécom — Espace Découverte
Prototype Streamlit complet
"""

import streamlit as st
import time

# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Espace Découverte – Algérie Télécom",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# GLOBAL CSS
# ──────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&family=Space+Mono:wght@400;700&display=swap');

    /* ---- Root variables ---- */
    :root {
        --at-green:  #00a651;
        --at-dark:   #003d20;
        --at-light:  #e8f5ee;
        --at-accent: #ff6b00;
        --at-gray:   #f4f6f5;
        --at-text:   #1a2e22;
        --radius: 14px;
    }

    /* ---- Global ---- */
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        color: var(--at-text);
    }
    .stApp { background: #f0f7f3; }

    /* ---- Hide Streamlit chrome ---- */
    #MainMenu, footer, header { visibility: hidden; }

    /* ---- Sidebar ---- */
    [data-testid="stSidebar"] {
        background: var(--at-dark) !important;
        border-right: 3px solid var(--at-green);
    }
    [data-testid="stSidebar"] * { color: #d4f0df !important; }
    [data-testid="stSidebar"] .stRadio label { font-size: 15px; }

    /* ---- Hero banner ---- */
    .hero {
        background: linear-gradient(135deg, var(--at-dark) 0%, #005c30 60%, var(--at-green) 100%);
        border-radius: var(--radius);
        padding: 48px 40px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }
    .hero::before {
        content: '';
        position: absolute; top: -60px; right: -60px;
        width: 260px; height: 260px;
        border-radius: 50%;
        background: rgba(255,255,255,0.06);
    }
    .hero h1 { color: white; font-size: 2.4rem; font-weight: 900; margin: 0 0 8px; }
    .hero p  { color: #a8e6c0; font-size: 1.1rem; margin: 0; }
    .hero .badge {
        display: inline-block;
        background: var(--at-accent);
        color: white; font-weight: 700; font-size: 12px;
        padding: 4px 12px; border-radius: 20px;
        margin-bottom: 12px; letter-spacing: 1px; text-transform: uppercase;
    }

    /* ---- Section title ---- */
    .section-title {
        font-size: 1.35rem; font-weight: 700;
        color: var(--at-dark); border-left: 4px solid var(--at-green);
        padding-left: 12px; margin: 28px 0 16px;
    }

    /* ---- App / Platform cards ---- */
    .card {
        background: white;
        border-radius: var(--radius);
        padding: 20px;
        box-shadow: 0 2px 12px rgba(0,61,32,0.10);
        transition: transform .2s, box-shadow .2s;
        height: 100%;
        border-top: 4px solid var(--at-green);
    }
    .card:hover { transform: translateY(-4px); box-shadow: 0 8px 24px rgba(0,61,32,0.18); }
    .card .emoji { font-size: 2.2rem; }
    .card h3 { margin: 8px 0 4px; font-size: 1.05rem; color: var(--at-dark); }
    .card p  { font-size: 0.88rem; color: #5a6e60; margin: 0; line-height: 1.5; }
    .card .tag {
        display: inline-block; margin-top: 10px;
        background: var(--at-light); color: var(--at-dark);
        font-size: 11px; font-weight: 700; padding: 3px 10px;
        border-radius: 20px; letter-spacing: .5px;
    }
    .card .tag.web { background: #fff3e0; color: #bf5000; }

    /* ---- Demo steps ---- */
    .step {
        background: white;
        border-radius: var(--radius);
        padding: 16px 20px;
        margin-bottom: 12px;
        border-left: 5px solid var(--at-green);
        box-shadow: 0 1px 6px rgba(0,61,32,0.08);
        display: flex; align-items: flex-start; gap: 12px;
    }
    .step .num {
        background: var(--at-green); color: white;
        font-weight: 900; font-size: 1.1rem;
        width: 34px; height: 34px; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        flex-shrink: 0;
    }
    .step .content h4 { margin: 0 0 4px; font-size: 0.97rem; color: var(--at-dark); }
    .step .content p  { margin: 0; font-size: 0.85rem; color: #6a7e70; }

    /* ---- FAQ accordion ---- */
    .faq-q {
        background: white;
        border-radius: 10px;
        padding: 14px 18px;
        margin-bottom: 8px;
        box-shadow: 0 1px 5px rgba(0,61,32,0.07);
        font-weight: 600; color: var(--at-dark); font-size: 0.95rem;
    }

    /* ---- Stat pill ---- */
    .stat-pill {
        background: var(--at-dark);
        color: white; border-radius: 50px;
        padding: 14px 22px; text-align: center;
        margin-bottom: 10px;
    }
    .stat-pill .number { font-size: 2rem; font-weight: 900; color: var(--at-green); display: block; }
    .stat-pill .label  { font-size: 0.82rem; opacity: .8; }

    /* ---- Satisfaction bar ---- */
    .bar-wrap { margin-bottom: 10px; }
    .bar-label { font-size: 0.88rem; margin-bottom: 4px; color: var(--at-dark); font-weight: 600; }
    .bar-bg { background: #d0e8d8; border-radius: 6px; height: 14px; }
    .bar-fill { background: var(--at-green); border-radius: 6px; height: 14px; }

    /* ---- KPI card ---- */
    .kpi {
        background: white; border-radius: var(--radius);
        padding: 18px; text-align: center;
        box-shadow: 0 2px 10px rgba(0,61,32,0.09);
        border-bottom: 4px solid var(--at-green);
    }
    .kpi .val { font-size: 2rem; font-weight: 900; color: var(--at-green); }
    .kpi .lbl { font-size: 0.82rem; color: #5a6e60; margin-top: 4px; }

    /* ---- Buttons ---- */
    .stButton>button {
        background: var(--at-green) !important;
        color: white !important; font-weight: 700 !important;
        border: none !important; border-radius: 8px !important;
        padding: 8px 22px !important;
        transition: background .2s !important;
    }
    .stButton>button:hover { background: var(--at-dark) !important; }

    /* ---- Form inputs ---- */
    .stTextInput input, .stSelectbox select, .stTextArea textarea {
        border-radius: 8px !important;
        border: 1.5px solid #b8d8c3 !important;
    }
    .stTextInput input:focus, .stSelectbox select:focus {
        border-color: var(--at-green) !important;
        box-shadow: 0 0 0 2px rgba(0,166,81,0.15) !important;
    }

    /* ---- Progress ---- */
    .stProgress > div > div { background-color: var(--at-green) !important; }

    /* ---- Success / info ---- */
    .success-box {
        background: var(--at-light); border-left: 4px solid var(--at-green);
        border-radius: 8px; padding: 14px 18px;
        font-size: 0.92rem; color: var(--at-dark);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────
# DATA
# ──────────────────────────────────────────────
APPS = [
    {
        "emoji": "📱",
        "name": "My iDOOM",
        "desc": "Gérez votre ligne ADSL/FTTH : paiement de facture, consultation du solde, signalement de panne.",
        "type": "Application native",
        "store": "https://play.google.com/store",
    },
    {
        "emoji": "💳",
        "name": "E-Paiement",
        "desc": "Payez vos factures Algérie Télécom en ligne rapidement et en toute sécurité.",
        "type": "Application native",
        "store": "https://play.google.com/store",
    },
    {
        "emoji": "🎬",
        "name": "Dzair Play",
        "desc": "Plateforme de streaming algérienne : films, séries et contenus locaux en VOD.",
        "type": "Application native",
        "store": "https://play.google.com/store",
    },
    {
        "emoji": "🛒",
        "name": "Idoom Market",
        "desc": "Boutique en ligne officielle pour les équipements et offres internet d'Algérie Télécom.",
        "type": "Application native",
        "store": "https://play.google.com/store",
    },
    {
        "emoji": "📰",
        "name": "Veille Médias",
        "desc": "Agrégateur de presse et d'actualités numériques algériennes.",
        "type": "Application native",
        "store": "https://play.google.com/store",
    },
]

PLATFORMS = [
    {
        "emoji": "🎓",
        "name": "EduGato",
        "desc": "Plateforme e-learning nationale : cours en ligne pour tous les niveaux scolaires.",
        "type": "Plateforme web",
        "url": "https://edugato.dz",
    },
    {
        "emoji": "📚",
        "name": "MOALIM",
        "desc": "Espace numérique éducatif pour enseignants et élèves : ressources pédagogiques.",
        "type": "Plateforme web",
        "url": "https://moalim.dz",
    },
    {
        "emoji": "💬",
        "name": "Doruscom",
        "desc": "Plateforme de communication digitale pour entreprises et administrations algériennes.",
        "type": "Plateforme web",
        "url": "https://doruscom.dz",
    },
]

FAQ_ITEMS = [
    ("Les applications sont-elles gratuites ?",
     "Oui, toutes les applications natives d'Algérie Télécom sont disponibles gratuitement sur Google Play et App Store."),
    ("Mes données personnelles sont-elles sécurisées ?",
     "Absolument. Nous utilisons le chiffrement SSL/TLS et l'authentification à deux facteurs. Vos données ne sont jamais vendues à des tiers."),
    ("Quelle est la différence entre une application et une plateforme web ?",
     "Les applications se téléchargent sur votre smartphone. Les plateformes web sont accessibles directement via un navigateur internet, sans installation."),
    ("Que faire si j'ai un problème avec My iDOOM ?",
     "Rendez-vous dans la section Support de l'application, ou contactez le 1522. Un technicien vous assistera sous 24h."),
    ("Puis-je payer ma facture sans me déplacer en agence ?",
     "Oui ! Avec My iDOOM ou E-Paiement, réglez votre facture en moins de 2 minutes depuis votre smartphone ou ordinateur."),
    ("Comment m'inscrire à EduGato ?",
     "Visitez edugato.dz, cliquez sur « S'inscrire », renseignez votre adresse e-mail et créez un mot de passe. L'accès est immédiat."),
]

DEMO_STEPS = {
    "Payer une facture": [
        ("Connexion", "Saisissez votre numéro de ligne et mot de passe pour accéder à votre espace."),
        ("Mes factures", "Appuyez sur « Factures » dans le menu principal. La liste de vos factures s'affiche."),
        ("Choisir la facture", "Sélectionnez la facture à régler. Le montant et la date d'échéance apparaissent."),
        ("Paiement", "Choisissez votre mode de paiement : carte CIB / Dahabia, puis confirmez."),
        ("Confirmation", "Un SMS et une notification de confirmation vous sont envoyés instantanément. ✅"),
    ],
    "Consulter ma consommation": [
        ("Accueil", "Depuis l'accueil My iDOOM, votre consommation du mois en cours est affichée en direct."),
        ("Détails", "Appuyez sur « Consommation » pour voir l'historique des 6 derniers mois."),
        ("Graphiques", "Un graphique interactif montre votre évolution de consommation mensuelle."),
        ("Alertes", "Activez les notifications pour recevoir une alerte à 80 % de votre quota."),
    ],
    "Signaler une panne": [
        ("Menu", "Ouvrez My iDOOM et appuyez sur « Support » puis « Signaler une panne »."),
        ("Description", "Décrivez le problème (coupure totale, lenteur, wi-fi instable…) et joignez une capture si besoin."),
        ("Envoi", "Validez. Un numéro de ticket vous est attribué automatiquement."),
        ("Suivi", "Suivez l'état de votre ticket en temps réel depuis l'application. Délai moyen : 24–48h."),
    ],
}

TUTORIALS = [
    ("📹", "Payer une facture avec My iDOOM", "1 min 12 s", "#"),
    ("📹", "Consulter sa consommation internet", "58 s", "#"),
    ("📹", "Signaler une panne depuis l'application", "1 min 04 s", "#"),
    ("📹", "S'inscrire sur EduGato", "1 min 30 s", "#"),
    ("📹", "Accéder à MOALIM / Doruscom", "47 s", "#"),
]

# ──────────────────────────────────────────────
# SIDEBAR NAVIGATION
# ──────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div style='text-align:center; padding: 20px 0 10px;'>
            <div style='font-size:2.8rem;'>🌐</div>
            <div style='font-weight:900; font-size:1.1rem; color:white; margin-top:4px;'>
                Espace Découverte
            </div>
            <div style='font-size:0.78rem; color:#80c49a; margin-top:2px;'>
                Algérie Télécom
            </div>
        </div>
        <hr style='border-color:#1a5c32; margin:12px 0 20px;'>
        """,
        unsafe_allow_html=True,
    )

    page = st.radio(
        "Navigation",
        [
            "🏠  Accueil",
            "📱  Nos Services",
            "🎮  Démo Interactive",
            "🎬  Tutoriels Vidéo",
            "❓  FAQ",
            "📊  Tableau de bord",
            "💬  Satisfaction",
        ],
        label_visibility="collapsed",
    )

    st.markdown(
        """
        <hr style='border-color:#1a5c32; margin:20px 0 12px;'>
        <div style='font-size:0.78rem; color:#6aab80; text-align:center; padding-bottom:12px;'>
            🔒 Données sécurisées · SSL/TLS<br>
            © 2025 Algérie Télécom
        </div>
        """,
        unsafe_allow_html=True,
    )

# ──────────────────────────────────────────────
# SESSION STATE
# ──────────────────────────────────────────────
if "demo_step" not in st.session_state:
    st.session_state.demo_step = 0
if "demo_flow" not in st.session_state:
    st.session_state.demo_flow = "Payer une facture"
if "satisfaction_submitted" not in st.session_state:
    st.session_state.satisfaction_submitted = False
if "visitors" not in st.session_state:
    st.session_state.visitors = 1284
if "conversions" not in st.session_state:
    st.session_state.conversions = 347

# ──────────────────────────────────────────────
# PAGE: ACCUEIL
# ──────────────────────────────────────────────
if "Accueil" in page:
    st.markdown(
        """
        <div class="hero">
            <span class="badge">Nouveau</span>
            <h1>🌐 Espace Découverte</h1>
            <p>Découvrez, testez et adoptez tous les services numériques d'Algérie Télécom<br>
            — sans téléchargement, depuis n'importe quel support.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    stats = [
        ("5", "Applications mobiles"),
        ("3", "Plateformes web"),
        ("90%", "Gain de temps perçu"),
        ("55%", "Non-utilisateurs à sensibiliser"),
    ]
    for col, (val, lbl) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(
                f"""<div class="kpi"><div class="val">{val}</div><div class="lbl">{lbl}</div></div>""",
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-title">Pourquoi cet espace ?</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    reasons = [
        ("🔍", "Découverte sans installation", "Explorez toutes nos applications et plateformes directement depuis votre navigateur, sans rien télécharger."),
        ("🎮", "Démo interactive", "Simulez les parcours clés (paiement, signalement de panne…) pour vous familiariser en toute confiance."),
        ("📺", "Tutoriels courts", "Des vidéos d'une minute pour apprendre à utiliser chaque service pas à pas."),
    ]
    for col, (ic, title, desc) in zip([c1, c2, c3], reasons):
        with col:
            st.markdown(
                f"""<div class="card"><div class="emoji">{ic}</div>
                <h3>{title}</h3><p>{desc}</p></div>""",
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-title">Accès multicanal</div>', unsafe_allow_html=True)
    channels = [
        ("💻", "Ordinateur", "www.algerietelecom.dz/espace-decouverte", "Clients moins à l'aise avec le mobile"),
        ("📱", "Smartphone / Tablette", "Version responsive du même site", "Clients voulant découvrir avant d'installer"),
        ("🏪", "Bornes en agence", "Application kiosque avec ambassadeur digital", "Clients attachés au canal physique"),
        ("📄", "Facture papier", "QR code renvoyant vers l'URL", "Tous les clients recevant une facture papier"),
    ]
    cols = st.columns(4)
    for col, (ic, name, access, target) in zip(cols, channels):
        with col:
            st.markdown(
                f"""<div class="card">
                <div class="emoji">{ic}</div>
                <h3>{name}</h3>
                <p><strong>Accès :</strong> {access}<br><br>
                <strong>Public :</strong> {target}</p>
                </div>""",
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-title">Alignement stratégique</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="success-box">
        🇩🇿 Cette proposition s'inscrit dans la <strong>Stratégie nationale de transformation numérique 2025-2030</strong>
        en favorisant l'inclusion numérique, la dématérialisation des services et la réduction de la fracture numérique.
        Elle répond aux objectifs d'Algérie Télécom : moderniser l'expérience client, promouvoir les paiements
        électroniques et développer l'éducation numérique.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ──────────────────────────────────────────────
# PAGE: NOS SERVICES
# ──────────────────────────────────────────────
elif "Services" in page:
    st.markdown(
        """<div class="hero">
        <h1>📱 Nos Services Numériques</h1>
        <p>5 applications mobiles et 3 plateformes web pour simplifier votre quotidien.</p>
        </div>""",
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">📱 Applications Natives</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    for i, app in enumerate(APPS):
        with cols[i % 3]:
            st.markdown(
                f"""<div class="card">
                <div class="emoji">{app['emoji']}</div>
                <h3>{app['name']}</h3>
                <p>{app['desc']}</p>
                <span class="tag">📱 {app['type']}</span>
                </div><br>""",
                unsafe_allow_html=True,
            )
            if st.button(f"⬇️ Télécharger {app['name']}", key=f"dl_{i}"):
                st.success(f"✅ Redirection vers le store pour {app['name']}…")

    st.markdown('<div class="section-title">🌐 Plateformes Web</div>', unsafe_allow_html=True)
    cols2 = st.columns(3)
    for i, plat in enumerate(PLATFORMS):
        with cols2[i]:
            st.markdown(
                f"""<div class="card">
                <div class="emoji">{plat['emoji']}</div>
                <h3>{plat['name']}</h3>
                <p>{plat['desc']}</p>
                <span class="tag web">🌐 {plat['type']}</span>
                </div><br>""",
                unsafe_allow_html=True,
            )
            if st.button(f"🔗 Accéder à {plat['name']}", key=f"web_{i}"):
                st.success(f"✅ Ouverture de {plat['url']}")

    st.markdown('<div class="section-title">My iDOOM — Fonctionnalités détaillées</div>', unsafe_allow_html=True)
    st.markdown(
        """Plébiscitée par **57,6 %** des utilisateurs, My iDOOM est l'application la plus utile.
        Voici ses fonctionnalités clés :"""
    )

    feats = [
        ("💰", "Paiement de facture", "Réglez vos factures internet en quelques secondes."),
        ("📊", "Consultation du solde", "Visualisez votre consommation en temps réel."),
        ("🚨", "Signalement de panne", "Déclarez une panne et suivez l'intervention."),
        ("📜", "Historique des paiements", "Accédez à vos factures des 12 derniers mois."),
        ("🔔", "Notifications personnalisées", "Alertes d'échéance et de quota."),
        ("💬", "Support intégré", "Chat en direct et système de tickets."),
    ]
    c1, c2, c3 = st.columns(3)
    for j, (ic, title, desc) in enumerate(feats):
        with [c1, c2, c3][j % 3]:
            st.markdown(
                f"""<div class="card"><div class="emoji">{ic}</div>
                <h3>{title}</h3><p>{desc}</p></div><br>""",
                unsafe_allow_html=True,
            )

# ──────────────────────────────────────────────
# PAGE: DÉMO INTERACTIVE
# ──────────────────────────────────────────────
elif "Démo" in page:
    st.markdown(
        """<div class="hero">
        <h1>🎮 Démo Interactive</h1>
        <p>Simulez les parcours clés de My iDOOM — sans téléchargement ni inscription.</p>
        </div>""",
        unsafe_allow_html=True,
    )

    flow = st.selectbox(
        "Choisissez un parcours à simuler :",
        list(DEMO_STEPS.keys()),
        key="demo_flow_select",
    )
    if flow != st.session_state.demo_flow:
        st.session_state.demo_flow = flow
        st.session_state.demo_step = 0

    steps = DEMO_STEPS[st.session_state.demo_flow]
    total = len(steps)
    current = st.session_state.demo_step

    st.markdown(
        f"""<div style='margin: 16px 0 8px; font-size:0.9rem; color:#5a6e60;'>
        Étape {min(current+1, total)} sur {total}</div>""",
        unsafe_allow_html=True,
    )
    st.progress((current) / total)

    # Show all steps up to current
    for i, (title, desc) in enumerate(steps):
        is_active = i == current
        is_done = i < current
        color = "var(--at-green)" if is_done else ("#005c30" if is_active else "#c8ddd0")
        opacity = "1" if i <= current else "0.4"
        icon = "✅" if is_done else ("▶️" if is_active else f"{i+1}")
        st.markdown(
            f"""<div class="step" style="opacity:{opacity}; border-left-color:{color};">
            <div class="num" style="background:{color};">{icon}</div>
            <div class="content">
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
            </div>""",
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col_prev, col_next, col_reset = st.columns([1, 1, 1])

    with col_prev:
        if st.button("⬅️ Précédent", disabled=(current == 0)):
            st.session_state.demo_step -= 1
            st.rerun()

    with col_next:
        if current < total:
            label = "Suivant ➡️" if current < total - 1 else "Terminer ✅"
            if st.button(label):
                st.session_state.demo_step = min(current + 1, total)
                st.rerun()

    with col_reset:
        if st.button("🔄 Recommencer"):
            st.session_state.demo_step = 0
            st.rerun()

    if current == total:
        st.balloons()
        st.markdown(
            f"""<div class="success-box">
            🎉 <strong>Félicitations !</strong> Vous avez complété le parcours <em>"{st.session_state.demo_flow}"</em>.<br>
            Prêt(e) à l'utiliser dans la vraie application ? Téléchargez <strong>My iDOOM</strong> maintenant !
            </div>""",
            unsafe_allow_html=True,
        )
        if st.button("⬇️ Télécharger My iDOOM"):
            st.success("✅ Redirection vers le Play Store / App Store…")

# ──────────────────────────────────────────────
# PAGE: TUTORIELS
# ──────────────────────────────────────────────
elif "Tutoriels" in page:
    st.markdown(
        """<div class="hero">
        <h1>🎬 Tutoriels Vidéo</h1>
        <p>Apprenez en moins d'une minute grâce à nos tutoriels pratiques.</p>
        </div>""",
        unsafe_allow_html=True,
    )

    for ic, title, duration, url in TUTORIALS:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(
                f"""<div class="step">
                <div class="num" style="background:#003d20; font-size:1.4rem; width:42px; height:42px;">{ic}</div>
                <div class="content">
                    <h4>{title}</h4>
                    <p>⏱️ Durée : {duration}</p>
                </div>
                </div>""",
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button(f"▶️ Visionner", key=f"tuto_{title[:8]}"):
                st.info(f"▶️ Lancement du tutoriel : **{title}**")
                with st.spinner("Chargement de la vidéo…"):
                    time.sleep(1.2)
                st.success("✅ La vidéo se lance dans un nouvel onglet.")

    st.markdown('<div class="section-title">📢 Vous préférez la démo en direct ?</div>', unsafe_allow_html=True)
    st.markdown(
        """<div class="success-box">
        🏪 Rendez-vous dans l'une de nos <strong>agences équipées de bornes tactiles</strong>.
        Un <strong>ambassadeur digital</strong> formé vous accompagnera et vous remettra un QR code
        personnalisé pour accéder directement à l'Espace Découverte depuis votre smartphone.
        </div>""",
        unsafe_allow_html=True,
    )

# ──────────────────────────────────────────────
# PAGE: FAQ
# ──────────────────────────────────────────────
elif "FAQ" in page:
    st.markdown(
        """<div class="hero">
        <h1>❓ Foire Aux Questions</h1>
        <p>Toutes les réponses à vos questions sur nos services numériques.</p>
        </div>""",
        unsafe_allow_html=True,
    )

    search = st.text_input("🔍 Rechercher une question…", placeholder="ex: sécurité, paiement, gratuit…")

    filtered = [
        (q, a) for q, a in FAQ_ITEMS
        if search.lower() in q.lower() or search.lower() in a.lower()
    ] if search else FAQ_ITEMS

    if not filtered:
        st.warning("Aucun résultat trouvé. Essayez un autre mot-clé.")
    else:
        for i, (question, answer) in enumerate(filtered):
            with st.expander(f"❓ {question}"):
                st.markdown(
                    f"""<div class="success-box">💬 {answer}</div>""",
                    unsafe_allow_html=True,
                )

    st.markdown('<div class="section-title">Vous n\'avez pas trouvé votre réponse ?</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """<div class="card">
            <div class="emoji">📞</div>
            <h3>Support téléphonique</h3>
            <p>Appelez le <strong>1522</strong> (gratuit depuis une ligne AT)<br>
            Lun–Ven 8h–17h | Sam 8h–12h</p>
            </div>""",
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """<div class="card">
            <div class="emoji">🏪</div>
            <h3>En agence</h3>
            <p>Retrouvez votre agence Algérie Télécom la plus proche.<br>
            <strong>Ambassadeurs digitaux</strong> disponibles pour vous aider.</p>
            </div>""",
            unsafe_allow_html=True,
        )

# ──────────────────────────────────────────────
# PAGE: TABLEAU DE BORD
# ──────────────────────────────────────────────
elif "Tableau" in page:
    st.markdown(
        """<div class="hero">
        <h1>📊 Tableau de Bord</h1>
        <p>Indicateurs de suivi de l'Espace Découverte — mis à jour en temps réel.</p>
        </div>""",
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-title">KPIs principaux</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    kpis = [
        (str(st.session_state.visitors), "Visiteurs uniques"),
        (str(st.session_state.conversions), "Téléchargements"),
        (f"{round(st.session_state.conversions/st.session_state.visitors*100, 1)}%", "Taux de conversion"),
        ("3 min 42 s", "Temps moyen / session"),
    ]
    for col, (val, lbl) in zip([c1, c2, c3, c4], kpis):
        with col:
            st.markdown(
                f"""<div class="kpi"><div class="val">{val}</div><div class="lbl">{lbl}</div></div>""",
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-title">Clics vers les services</div>', unsafe_allow_html=True)

    click_data = {
        "My iDOOM": 48,
        "E-Paiement": 22,
        "Dzair Play": 14,
        "EduGato": 10,
        "Idoom Market": 6,
    }
    for name, pct in click_data.items():
        st.markdown(
            f"""<div class="bar-wrap">
            <div class="bar-label">{name} — {pct}%</div>
            <div class="bar-bg"><div class="bar-fill" style="width:{pct}%;"></div></div>
            </div>""",
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-title">Freins à l\'adoption (non-utilisateurs)</div>', unsafe_allow_html=True)

    barriers = {
        "Ne connaissent pas les applications": 55.1,
        "Préfèrent se déplacer en agence": 24.5,
        "Trouvent l'application trop compliquée": 10.2,
        "Manque de confiance numérique": 6.1,
        "Autre": 4.1,
    }
    for name, pct in barriers.items():
        st.markdown(
            f"""<div class="bar-wrap">
            <div class="bar-label">{name} — {pct}%</div>
            <div class="bar-bg">
            <div class="bar-fill" style="width:{pct}%; background: {'#ff6b00' if pct > 30 else 'var(--at-green)'};"></div>
            </div></div>""",
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section-title">Simulation — Impact de la campagne</div>', unsafe_allow_html=True)
    budget = st.slider("Budget communication (milliers DZD)", 100, 5000, 500, 100)
    estimated_reach = int(budget * 4.2)
    estimated_conv = int(estimated_reach * 0.27)

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Clients touchés (estimé)", f"{estimated_reach:,}", delta=None)
    with col_b:
        st.metric("Nouveaux utilisateurs (estimé)", f"{estimated_conv:,}", delta=None)
    with col_c:
        st.metric("Coût / nouvel utilisateur", f"{round(budget*1000/max(estimated_conv,1))} DZD", delta=None)

    st.markdown('<div class="section-title">Source des données de suivi</div>', unsafe_allow_html=True)
    sources = [
        ("👥", "Visiteurs uniques", "Google Analytics"),
        ("🔗", "Taux de clic apps", "Suivi des liens"),
        ("🔗", "Taux de clic web", "Suivi des liens"),
        ("⚙️", "Interactions démo", "Logs serveur"),
        ("⏱️", "Temps sur plateforme", "Google Analytics"),
        ("📈", "Taux de conversion", "Analytics × données internes"),
        ("⭐", "Satisfaction visiteurs", "Questionnaire intégré"),
    ]
    c1, c2 = st.columns(2)
    for j, (ic, indicator, source) in enumerate(sources):
        with [c1, c2][j % 2]:
            st.markdown(
                f"""<div class="step">
                <div class="num" style="background:#005c30;">{ic}</div>
                <div class="content"><h4>{indicator}</h4><p>Source : {source}</p></div>
                </div>""",
                unsafe_allow_html=True,
            )

# ──────────────────────────────────────────────
# PAGE: SATISFACTION
# ──────────────────────────────────────────────
elif "Satisfaction" in page:
    st.markdown(
        """<div class="hero">
        <h1>💬 Votre Avis Compte</h1>
        <p>Aidez-nous à améliorer l'Espace Découverte en répondant à ce court questionnaire.</p>
        </div>""",
        unsafe_allow_html=True,
    )

    if st.session_state.satisfaction_submitted:
        st.balloons()
        st.markdown(
            """<div class="success-box" style="font-size:1.05rem; padding: 20px 24px;">
            🎉 <strong>Merci pour votre retour !</strong><br><br>
            Votre avis nous aide à améliorer continuellement nos services numériques.
            N'hésitez pas à télécharger <strong>My iDOOM</strong> pour profiter
            de tous nos services directement depuis votre smartphone.
            </div>""",
            unsafe_allow_html=True,
        )
        if st.button("🔄 Soumettre un nouvel avis"):
            st.session_state.satisfaction_submitted = False
            st.rerun()
    else:
        with st.container():
            st.markdown('<div class="section-title">Questionnaire de satisfaction</div>', unsafe_allow_html=True)

            satisfaction = st.select_slider(
                "Comment évaluez-vous votre expérience sur l'Espace Découverte ?",
                options=["😞 Très mauvais", "😕 Mauvais", "😐 Moyen", "🙂 Bien", "😄 Excellent"],
                value="🙂 Bien",
            )

            services_used = st.multiselect(
                "Quels services avez-vous découverts aujourd'hui ?",
                [a["name"] for a in APPS] + [p["name"] for p in PLATFORMS],
            )

            tried_demo = st.radio(
                "Avez-vous essayé la démo interactive ?",
                ["Oui, c'était très utile", "Oui, mais c'était difficile à comprendre", "Non"],
                horizontal=True,
            )

            intention = st.radio(
                "Suite à votre visite, avez-vous l'intention de…",
                [
                    "Télécharger My iDOOM",
                    "Utiliser E-Paiement pour ma prochaine facture",
                    "Visiter EduGato / MOALIM",
                    "Aucune des propositions",
                ],
            )

            suggestion = st.text_area(
                "Une suggestion ou une remarque ? (optionnel)",
                placeholder="Votre avis nous est précieux…",
            )

            profile = st.selectbox(
                "Votre profil :",
                ["Particulier", "Professionnel / Entreprise", "Enseignant / Étudiant", "Retraité", "Autre"],
            )

            col1, col2 = st.columns([1, 2])
            with col1:
                if st.button("✅ Soumettre mon avis"):
                    with st.spinner("Enregistrement de votre avis…"):
                        time.sleep(1)
                    st.session_state.satisfaction_submitted = True
                    st.session_state.visitors += 1
                    if "Télécharger" in intention or "Paiement" in intention:
                        st.session_state.conversions += 1
                    st.rerun()

        st.markdown('<div class="section-title">Résultats agrégés (aperçu)</div>', unsafe_allow_html=True)
        st.markdown(
            """*Ces données sont issues de l'étude empirique menée auprès des clients d'Algérie Télécom.*"""
        )

        satisfaction_scores = {
            "😄 Excellent": 42,
            "🙂 Bien": 34,
            "😐 Moyen": 15,
            "😕 Mauvais": 6,
            "😞 Très mauvais": 3,
        }
        for label, pct in satisfaction_scores.items():
            st.markdown(
                f"""<div class="bar-wrap">
                <div class="bar-label">{label} — {pct}%</div>
                <div class="bar-bg"><div class="bar-fill" style="width:{pct}%;"></div></div>
                </div>""",
                unsafe_allow_html=True,
            )
