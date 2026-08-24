TETE = '<header class="tete">\n  <div class="enveloppe">\n    <a class="marque" href="index.html">Haario</a>\n    <div class="barre">\n      <nav class="nav" aria-label="Principale">\n        <a href="index.html" data-i18n="nav.accueil">Accueil</a>\n        <a href="charte.html"{c_charte} data-i18n="nav.charte">Charte</a>\n        <a href="confidentialite.html"{c_conf} data-i18n="nav.conf">ConfidentialitÃ©</a>\n        <a href="suppression-de-compte.html"{c_supp} data-i18n="nav.supp">Supprimer un compte</a>\n      </nav>\n      <div class="reglages">\n        <select class="choix-langue" id="langue" data-i18n-aria="a11y.langue" aria-label="Choisir la langue">\n          <option value="fr">FranÃ§ais</option>\n          <option value="en">English</option>\n          <option value="es">EspaÃ±ol</option>\n          <option value="ar">Ø§Ù„Ø¹Ø±Ø¨ÙŠØ©</option>\n        </select>\n        <button class="bouton-theme" id="theme" type="button" data-i18n-aria="a11y.theme" aria-label="Changer de thÃ¨me">\n          <svg class="soleil" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.6v2M12 19.4v2M2.6 12h2M19.4 12h2M5.4 5.4l1.4 1.4M17.2 17.2l1.4 1.4M18.6 5.4l-1.4 1.4M6.8 17.2l-1.4 1.4"/></svg>\n          <svg class="lune" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.2 8.2 0 0 1 9.5 4a8.3 8.3 0 1 0 10.5 10.5z"/></svg>\n        </button>\n      </div>\n    </div>\n  </div>\n</header>'
SCRIPT = '<script>\nvar CHROME = {\n  en: { "saut":"Skip to content","nav.accueil":"Home","nav.charte":"Terms","nav.conf":"Privacy","nav.supp":"Delete an account",\n        "a11y.langue":"Choose language","a11y.theme":"Switch theme",\n        "bandeau":"This document is published in French. The French version is the legally binding one. For a question in English, write to <a href=\\"mailto:contact@haarioai.fr\\">contact@haarioai.fr</a>.",\n        "pied.mentions":"Haario â€” service published by Mr Wajdi MRABTI. Postal address provided on request at <a href=\\"mailto:contact@haarioai.fr\\">contact@haarioai.fr</a>.",\n        "pied.charte":"Terms of use","pied.conf":"Privacy policy","pied.supp":"Delete an account","pied.contact":"Write to us" },\n  es: { "saut":"Ir al contenido","nav.accueil":"Inicio","nav.charte":"Condiciones","nav.conf":"Privacidad","nav.supp":"Eliminar una cuenta",\n        "a11y.langue":"Elegir idioma","a11y.theme":"Cambiar de tema",\n        "bandeau":"Este documento se publica en francÃ©s. La versiÃ³n francesa es la que da fe. Para cualquier consulta en espaÃ±ol, escriba a <a href=\\"mailto:contact@haarioai.fr\\">contact@haarioai.fr</a>.",\n        "pied.mentions":"Haario â€” servicio editado por D. Wajdi MRABTI. DirecciÃ³n postal facilitada previa solicitud en <a href=\\"mailto:contact@haarioai.fr\\">contact@haarioai.fr</a>.",\n        "pied.charte":"Condiciones de uso","pied.conf":"PolÃ­tica de privacidad","pied.supp":"Eliminar una cuenta","pied.contact":"EscrÃ­banos" },\n  ar: { "saut":"Ø§Ù„Ø§Ù†ØªÙ‚Ø§Ù„ Ø¥Ù„Ù‰ Ø§Ù„Ù…Ø­ØªÙˆÙ‰","nav.accueil":"Ø§Ù„Ø±Ø¦ÙŠØ³ÙŠØ©","nav.charte":"Ø´Ø±ÙˆØ· Ø§Ù„Ø§Ø³ØªØ®Ø¯Ø§Ù…","nav.conf":"Ø§Ù„Ø®ØµÙˆØµÙŠØ©","nav.supp":"Ø­Ø°Ù Ø­Ø³Ø§Ø¨",\n        "a11y.langue":"Ø§Ø®ØªÙŠØ§Ø± Ø§Ù„Ù„ØºØ©","a11y.theme":"ØªØºÙŠÙŠØ± Ø§Ù„Ù…Ø¸Ù‡Ø±",\n        "bandeau":"Ù‡Ø°Ù‡ Ø§Ù„ÙˆØ«ÙŠÙ‚Ø© Ù…Ù†Ø´ÙˆØ±Ø© Ø¨Ø§Ù„ÙØ±Ù†Ø³ÙŠØ©ØŒ ÙˆØ§Ù„Ù†Ø³Ø®Ø© Ø§Ù„ÙØ±Ù†Ø³ÙŠØ© Ù‡ÙŠ Ø§Ù„Ù…Ø¹ØªÙ…Ø¯Ø© Ù‚Ø§Ù†ÙˆÙ†Ø§Ù‹. Ù„Ø£ÙŠ Ø³Ø¤Ø§Ù„ Ø¨Ø§Ù„Ø¹Ø±Ø¨ÙŠØ©ØŒ Ø±Ø§Ø³Ù„ÙˆÙ†Ø§ Ø¹Ù„Ù‰ <a href=\\"mailto:contact@haarioai.fr\\">contact@haarioai.fr</a>.",\n        "pied.mentions":"Ù‡Ø§Ø±ÙŠÙˆ â€” Ø®Ø¯Ù…Ø© ÙŠØµØ¯Ø±Ù‡Ø§ Ø§Ù„Ø³ÙŠØ¯ ÙˆØ¬Ø¯ÙŠ Ø§Ù„Ù…Ø±Ø§Ø¨Ø·ÙŠ. ÙŠÙÙ‚Ø¯ÙŽÙ‘Ù… Ø§Ù„Ø¹Ù†ÙˆØ§Ù† Ø§Ù„Ø¨Ø±ÙŠØ¯ÙŠ Ø¹Ù†Ø¯ Ø§Ù„Ø·Ù„Ø¨ Ø¹Ù„Ù‰ <a href=\\"mailto:contact@haarioai.fr\\">contact@haarioai.fr</a>.",\n        "pied.charte":"Ø´Ø±ÙˆØ· Ø§Ù„Ø§Ø³ØªØ®Ø¯Ø§Ù…","pied.conf":"Ø³ÙŠØ§Ø³Ø© Ø§Ù„Ø®ØµÙˆØµÙŠØ©","pied.supp":"Ø­Ø°Ù Ø­Ø³Ø§Ø¨","pied.contact":"Ø±Ø§Ø³Ù„ÙˆÙ†Ø§" }\n};\n\n(function () {\n  var racine = document.documentElement;\n  var selecteur = document.getElementById(\'langue\');\n  var bouton = document.getElementById(\'theme\');\n\n  var ORIGINE = {};\n  document.querySelectorAll(\'[data-i18n]\').forEach(function (n) {\n    ORIGINE[n.getAttribute(\'data-i18n\')] = n.innerHTML;\n  });\n\n  // âš ï¸ Seule l\'interface est traduite. Le texte juridique reste en franÃ§ais :\n  //    une traduction non relue engagerait autant que l\'original.\n  function appliquerLangue(code) {\n    var dict = CHROME[code];\n    document.querySelectorAll(\'[data-i18n]\').forEach(function (n) {\n      var cle = n.getAttribute(\'data-i18n\');\n      var v = (dict && dict[cle] !== undefined) ? dict[cle] : ORIGINE[cle];\n      if (v !== undefined) n.innerHTML = v;\n    });\n    document.querySelectorAll(\'[data-i18n-aria]\').forEach(function (n) {\n      var cle = n.getAttribute(\'data-i18n-aria\');\n      if (dict && dict[cle]) n.setAttribute(\'aria-label\', dict[cle]);\n    });\n    var bandeau = document.getElementById(\'bandeau-langue\');\n    if (bandeau) bandeau.hidden = (code === \'fr\');\n    racine.lang = code;\n    racine.dir = (code === \'ar\' ? \'rtl\' : \'ltr\');\n    // Le corps du document reste en franÃ§ais quelle que soit l\'interface.\n    var doc = document.getElementById(\'contenu\');\n    if (doc) { doc.lang = \'fr\'; doc.dir = \'ltr\'; }\n    if (selecteur) selecteur.value = code;\n    try { localStorage.setItem(\'haario-langue\', code); } catch (e) {}\n  }\n\n  var depart = racine.lang;\n  try { depart = localStorage.getItem(\'haario-langue\') || depart; } catch (e) {}\n  if (!CHROME[depart] && depart !== \'fr\') depart = \'fr\';\n  appliquerLangue(depart);\n\n  if (selecteur) selecteur.addEventListener(\'change\', function () { appliquerLangue(this.value); });\n\n  if (bouton) bouton.addEventListener(\'click\', function () {\n    var actuel = racine.getAttribute(\'data-theme\');\n    if (!actuel) actuel = window.matchMedia(\'(prefers-color-scheme: dark)\').matches ? \'sombre\' : \'clair\';\n    var suivant = (actuel === \'sombre\' ? \'clair\' : \'sombre\');\n    racine.setAttribute(\'data-theme\', suivant);\n    try { localStorage.setItem(\'haario-theme\', suivant); } catch (e) {}\n  });\n})();\n</script>'
DEPART = "<script>\n(function () {\n  try {\n    var d = document.documentElement;\n    var t = localStorage.getItem('haario-theme');\n    if (t) d.setAttribute('data-theme', t);\n    var l = localStorage.getItem('haario-langue');\n    if (l) { d.lang = l; d.dir = (l === 'ar' ? 'rtl' : 'ltr'); }\n  } catch (e) {}\n})();\n</script>"
BANDEAU = '      <p class="bandeau-langue" id="bandeau-langue" data-i18n="bandeau" hidden>Ce document est publiÃ© en franÃ§ais, et la version franÃ§aise fait foi.</p>\n'
PIED = '<footer class="pied">\n  <div class="enveloppe">\n    <p class="mentions" data-i18n="pied.mentions">Haario â€” service Ã©ditÃ© par M. Wajdi MRABTI. Adresse postale communiquÃ©e sur demande Ã  <a href="mailto:contact@haarioai.fr">contact@haarioai.fr</a>.</p>\n    <nav aria-label="Documents">\n      <a href="charte.html" data-i18n="pied.charte">Charte d\'utilisation</a>\n      <a href="confidentialite.html" data-i18n="pied.conf">Politique de confidentialitÃ©</a>\n      <a href="suppression-de-compte.html" data-i18n="pied.supp">Supprimer un compte</a>\n      <a href="mailto:contact@haarioai.fr" data-i18n="pied.contact">Nous Ã©crire</a>\n    </nav>\n  </div>\n</footer>'


# -*- coding: utf-8 -*-
"""Genere confidentialite.html et charte.html depuis les .md relus.

    python3 gen.py

âš ï¸ Le texte juridique est repris VERBATIM des fichiers ../docs/*.md.
   Ne jamais editer les .html a la main : corriger le markdown, relancer.
   C'est ce qui empeche le site de diverger des documents soumis a Google.

âš ï¸ index.html et suppression-de-compte.html sont ecrits a la main : le style
   y est fige. Si styles.css change, les recopier.
"""
import io, os, re, markdown

CSS = io.open('styles.css', encoding='utf-8').read()

GABARIT = u"""<!DOCTYPE html>
<html lang="fr" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre} \u2014 Haario</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#F7F5FB" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121019" media="(prefers-color-scheme: dark)">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..700&family=Figtree:wght@400;500;700&family=Noto+Naskh+Arabic:wght@400;700&display=swap" rel="stylesheet">
<style>
{css}
</style>
{depart}
</head>
<body>

<a class="saut-contenu" href="#contenu" data-i18n="saut">Aller au contenu</a>

{tete}

<main id="contenu" class="doc" lang="fr" dir="ltr">
  <div class="enveloppe">
    <div class="colonne">
{bandeau}
{corps}
    </div>
  </div>
</main>

{pied}

{script}

</body>
</html>
"""

PAGES = [
    ("politique-de-confidentialite-haario.md", "confidentialite.html",
     u"Politique de confidentialit\u00e9",
     u"Comment Haario collecte, utilise, partage et conserve les donn\u00e9es des adolescents et de leurs parents."),
    ("charte-utilisation-haario.md", "charte.html",
     u"Charte d'utilisation",
     u"Les conditions d'utilisation de l'application Haario, pour l'adolescent comme pour le parent."),
]

for src, dest, titre, desc in PAGES:
    md = io.open(os.path.join('docs', src), encoding='utf-8').read()
    html = markdown.markdown(md, extensions=['tables', 'sane_lists'])
    html = html.replace('<table>', '<div class="tableau"><table>').replace('</table>', '</table></div>')
    html = html.replace('https://haarioai.com/confidentialite', 'confidentialite.html')
    html = html.replace('https://haarioai.com/suppression-de-compte', 'suppression-de-compte.html')
    html = re.sub(r'<p><strong>(Derni\u00e8re mise \u00e0 jour[^<]*)</strong></p>',
                  r'<p class="maj">\\1</p>', html, count=1)
    corps_html = u'\n'.join('      ' + l for l in html.splitlines())

    io.open(dest, 'w', encoding='utf-8', newline='\n').write(GABARIT.format(
        titre=titre, desc=desc, corps=corps_html, css=CSS,
        depart=DEPART, script=SCRIPT, pied=PIED, bandeau=BANDEAU,
        tete=TETE.format(
            c_charte=' aria-current="page"' if dest == 'charte.html' else '',
            c_conf=' aria-current="page"' if dest == 'confidentialite.html' else '',
            c_supp='')))
    print(dest, os.path.getsize(dest), 'octets')
