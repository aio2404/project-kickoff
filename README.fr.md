# Project Kickoff

**Un skill réutilisable pour démarrer un projet avec des profils d’agents séparés, un contexte ciblé et un premier résultat vérifié.**

[English](README.md) · [Guide d’utilisation](docs/usage.md) · [Sécurité](SECURITY.md)

Le skill accompagne le démarrage ou la reprise d’un projet. Si vous le demandez, Claude assure la conception et la relecture, puis lance directement Codex pour les tâches de développement. Ce sont des instructions : il ne lance aucun agent et ne crée aucune isolation à lui seul.

## Installation

Avec le gestionnaire tiers Skills CLI, si vous l’utilisez déjà :

```bash
npx skills add aio2404/project-kickoff --skill project-kickoff
```

Choisissez l’agent et le périmètre du projet. `npx` peut télécharger et exécuter ce gestionnaire tiers.

Vous pouvez aussi cloner le dépôt et copier uniquement `skills/project-kickoff` dans le dossier de skills du projet : `.claude/skills/project-kickoff/` pour Claude Code, ou `.agents/skills/project-kickoff/` pour Codex selon les règles de découverte de votre version. N’écrasez pas une installation existante. Relancez une session et vérifiez le chargement.

Un paquet plugin Claude est également fourni ; les commandes et limites sont détaillées dans le [README anglais](README.md#claude-code-plugin). Un profil isolé peut ne pas charger les skills installés globalement.

## Exemple de demande

```text
Utilise project-kickoff pour préparer ce projet. Je préfère le terminal.
Claude conçoit et relit ; il lance Codex pour réaliser les tâches.
Préserve l’existant. Demande avant une installation ou une modification hors projet.
Aucun commit ni publication. Commençons par un petit prototype avec des données fictives.
```

Dans Codex, utilisez `$project-kickoff`. Le skill s’adresse à l’utilisateur dans sa langue, même si ses instructions sont en anglais.

## Ce qu’il organise

1. Vérification du bon dossier, de l’existant et des choix déjà validés.
2. Préparation de profils Claude/Codex et contrôle de ce qu’ils chargent réellement.
3. Choix de skills utiles : Impeccable, webapp-testing et Superpowers sont des options pour un projet web, pas des dépendances imposées.
4. Essai de délégation délimité, puis cadrage du premier parcours.
5. Développement dans le périmètre approuvé, relecture et vérifications.
6. État de reprise court pour éviter de recommencer l’inventaire à chaque session.

## Limites importantes

Un profil séparé n’est pas une VM. Le skill ne bloque pas techniquement les lectures de fichiers, les accès réseau ou les actions externes. Les appels de modèles peuvent consommer un quota ou être facturés. L’hébergement, les données, les permissions et la conformité doivent être vérifiés séparément.

Le dépôt ne contient aucun installateur, hook ni client de modèle. Il ne redistribue pas les outils tiers. Ses vérifications automatiques contrôlent la structure et quelques motifs courants de données privées ; elles ne constituent ni un audit de sécurité complet ni une mesure d’efficacité des agents.

## Vérifier le dépôt

Avec Python 3.10 ou supérieur, sans dépendance supplémentaire :

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Projet indépendant, sous [licence MIT](LICENSE), sans affiliation à Anthropic ou OpenAI. Contributions bienvenues via [CONTRIBUTING.md](CONTRIBUTING.md).
