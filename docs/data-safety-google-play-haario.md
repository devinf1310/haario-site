# Déclaration de sécurité des données — Google Play (Data Safety)

À recopier tel quel dans Play Console > Contenu de l'app > Sécurité des données. Ce document doit rester identique, champ par champ, à la politique de confidentialité publiée. Toute divergence entre les deux est un motif de rejet.

## Identité et URL à renseigner

| Champ Play Console | Valeur |
|---|---|
| Responsable / éditeur | M. Wajdi MRABTI (personne physique — à remplacer par la société lors de sa création) |
| Adresse e-mail de contact | contact@haarioai.fr |
| URL de la politique de confidentialité | `https://haarioai.com/confidentialite` |
| URL de suppression de compte | `https://haarioai.com/suppression-de-compte` |
| URL des conditions d'utilisation | `https://haarioai.com/charte` |

> ⚠️ **Ces trois pages doivent être en ligne et accessibles sans authentification avant la soumission.** Google visite la page de suppression pendant la validation ; un lien mort bloque le processus.

## Collecte et partage de données — vue d'ensemble

**Cette app collecte-t-elle ou partage-t-elle des données utilisateur ?** Oui

**Toutes les données sont-elles chiffrées en transit ?** Oui

**L'utilisateur peut-il demander la suppression de ses données ?** Oui → renseigner l'URL de la page de suppression de compte (point 3)

## Détail par catégorie Google Play

### Informations personnelles

| Type de donnée | Collectée | Partagée | Finalité déclarée | Optionnelle/Obligatoire |
|---|---|---|---|---|
| Nom | Oui | Non | Fonctionnalité de l'app (personnalisation du compte) | Obligatoire |
| Adresse e-mail | Oui | Non | Fonctionnalité de l'app, communication (compte parent) | Obligatoire |
| Âge / date de naissance | Oui | Non | Fonctionnalité de l'app, conformité réglementaire | Obligatoire |

### Santé et fitness

| Type de donnée | Collectée | Partagée | Finalité déclarée | Optionnelle/Obligatoire |
|---|---|---|---|---|
| Informations de santé mentale | Oui | Oui — avec OpenAI (traitement du contenu), transmission au parent en cas de détresse | Fonctionnalité de l'app (repérage de signaux de mal-être, orientation vers un adulte) | Obligatoire pour le fonctionnement de l'app |

> C'est la catégorie la plus sensible du formulaire. Google demande ici une cohérence stricte avec la politique de confidentialité : la finalité déclarée doit reprendre exactement "repérage de signaux de mal-être / orientation", pas "diagnostic" ni "détection de trouble" (cf. la décision de qualification juridique — évitez tout vocabulaire médical ici aussi).

### Messages / contenu généré par l'utilisateur

| Type de donnée | Collectée | Partagée | Finalité déclarée | Optionnelle/Obligatoire |
|---|---|---|---|---|
| Contenu des conversations avec l'agent | Oui | Oui — avec OpenAI (génération des réponses) | Fonctionnalité de l'app | Obligatoire |

### Activité de l'application

| Type de donnée | Collectée | Partagée | Finalité déclarée | Optionnelle/Obligatoire |
|---|---|---|---|---|
| Interactions dans l'app | Oui | Non | Analytics interne, amélioration du produit | Optionnelle |
| Historique d'utilisation | Oui | Non | Fonctionnalité de l'app | Obligatoire |

### Identifiants de l'appareil ou autres identifiants

| Type de donnée | Collectée | Partagée | Finalité déclarée | Optionnelle/Obligatoire |
|---|---|---|---|---|
| Identifiants techniques (device ID, token Firebase) | Oui | Oui — avec Google Firebase (infrastructure) | Fonctionnalité de l'app, sécurité | Obligatoire |

## Durées de conservation

Ces durées doivent être identiques à celles de la section 5 de la politique de confidentialité.

| Catégorie de données | Durée |
|---|---|
| Données de compte | Durée de vie du compte + 30 jours après suppression |
| Contenu des échanges — aucune alerte émise | Durée de vie du compte + 30 jours après suppression |
| Contenu des échanges — une alerte a été émise sur la conversation | 6 mois à compter de l'émission de l'alerte, **même si le compte est supprimé avant ce délai** |
| Données de santé mentale / signaux de détresse | 6 mois à compter de la détection du signal |
| Extraits transmis aux parents | 6 mois à compter de la transmission |
| Données techniques | 13 mois |

> La conservation de six mois au-delà de la suppression du compte, pour les seules conversations ayant donné lieu à une alerte, doit apparaître **à l'identique** dans la politique de confidentialité et sur la page de suppression de compte. Une page de suppression qui annoncerait un effacement intégral immédiat contredirait cette déclaration : c'est une divergence que Google contrôle, la page de suppression étant visitée pendant la validation.

## Tranche d'âge et public visé

| Champ | Valeur |
|---|---|
| Public cible déclaré | Adolescents — à partir de 13 ans |
| Compte créé et détenu par | Le parent ou représentant légal |

> ⚠️ Le seuil du programme **Familles** de Google Play est à **moins de 13 ans**. Le public déclaré commençant désormais à 13 ans révolus, l'application n'y bascule plus automatiquement, et les obligations propres aux services destinés aux enfants ne s'appliquent plus de plein droit.
>
> Ce qui reste dû : le questionnaire **Public cible et contenu** de la Play Console, en déclarant les tranches 13-15 et 16-17 et en indiquant que l'application ne vise pas les enfants ; et la politique de confidentialité liée depuis la fiche Play, qui est exigée de toute application collectant des données personnelles, quel que soit l'âge.
>
> ⚠️ Point de vigilance : Google peut requalifier une application dont la présentation attire manifestement les enfants, même lorsque le public déclaré commence à 13 ans. La mascotte et l'univers coloré de la fiche comme du site sont ce qui sera regardé. **À vérifier avant soumission.**
>
> ⚠️ Ce seuil de 13 ans est celui de Google, et lui seul. **L'âge du consentement numérique reste fixé à 15 ans en France** : le consentement du parent ou représentant légal demeure requis pour tout utilisateur mineur, et rien de ce qui précède ne le modifie.

## Pratiques de sécurité des données à cocher

- [x] Les données sont chiffrées en transit
- [x] L'utilisateur peut demander la suppression des données
      → URL à renseigner : `https://haarioai.com/suppression-de-compte`
- [ ] Suivi d'un standard de sécurité indépendant — **laissé décoché : aucun audit indépendant n'existe à ce jour**

## Vérification de cohérence avant soumission

Avant de soumettre, relire les deux documents côte à côte sur ces points précis, car ce sont les divergences les plus fréquemment sanctionnées par Google :

1. **Les destinataires cités sont identiques** : OpenAI et Google Firebase doivent apparaître dans les deux documents, avec les mêmes finalités.
2. **Le champ "santé mentale" est bien déclaré comme catégorie de santé** dans Play (beaucoup d'équipes l'oublient et le classent par erreur en "contenu utilisateur" seulement — c'est un motif de rejet a posteriori si Google le détecte).
3. **La possibilité de suppression** est cochée "Oui" et pointe vers une URL active (voir point 3) — un lien mort ou une page inexistante bloque la validation.
4. **Le partage avec un tiers (OpenAI)** est bien déclaré comme "partage", pas seulement "traitement interne" — Google distingue les deux dans son formulaire, et sous-déclarer un partage est le motif de rejet le plus fréquent sur ce type d'app.
