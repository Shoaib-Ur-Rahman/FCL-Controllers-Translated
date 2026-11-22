# FCL Controllers — Translated Repository

[![Original project](https://img.shields.io/badge/Original-FCL--Team%2FFCL--Controllers-3776AB)](https://github.com/FCL-Team/FCL-Controllers)

This repository provides translated documentation and resources for the FCL Controllers project.

> [!IMPORTANT]
> This is an unofficial translated mirror. Controller content, original documentation, trademarks, and project credits belong to [FCL-Team](https://github.com/FCL-Team) and the respective contributors.

## About

FCL Controllers is the controller repository for FCL. It contains controller packages, JSON metadata, screenshots, icons, version information, and category data.

**Original repository:** [FCL-Team/FCL-Controllers](https://github.com/FCL-Team/FCL-Controllers)

## Download and usage

1. Open the original repository or this translated repository.
2. Download the controller ZIP or the complete source package.
3. Do not install content you do not trust or do not have permission to use.
4. Follow FCL's original upload and installation instructions.

## Contributing

Before contributing:

- Review the original project's upload rules.
- Upload only original or properly licensed work.
- Request permission before uploading another creator's controller.
- Ensure that each Pull Request changes only the relevant controller and its assets.
- Keep translated text clearly separate from original project JSON data.
- Never change IDs, paths, or JSON keys solely for translation purposes.

## Uploading a controller

A controller ZIP should be named using its controller ID:

```text
<controller_id>.zip
```

The package structure should look like this:

```text
/<controller_id>/
├── index.json
├── version.json
├── icon.png
├── versions/
│   └── <version_code>.json
└── screenshots/
    ├── 01.png
    ├── 02.png
    └── ...
```

### Required files

| Path | Purpose |
|---|---|
| `<controller_id>/index.json` | Controller ID, name, introduction, language, devices, and categories |
| `<controller_id>/version.json` | Screenshot count, description, author, latest version, and history |
| `<controller_id>/versions/<version_code>.json` | Configuration for a controller version |
| `<controller_id>/icon.png` | Controller icon |
| `<controller_id>/screenshots/01.png` | First screenshot |

### Requirements

- Use valid JSON syntax in `index.json` and `version.json`.
- Define all controller categories used by the controller.
- Include at least one screenshot.
- Number screenshots sequentially from `01` through `16`, if used.
- Keep the controller ZIP and internal file structure organized.
- Wait patiently if a manual review process is required.

## Updating an existing controller

For a new version:

1. Move the current `latest` object into `history`.
2. Replace `latest` with the new version code and name.
3. Update the screenshot count and description.
4. Add the new `versions/<version_code>.json` file.
5. Update only the relevant controller and its images.

Example `index.json` entry:

```json
{
  "id": "Example",
  "lang": "all",
  "name": "Example",
  "introduction": "Example controller",
  "device": [0, 1],
  "categories": [1]
}
```

Example `version.json`:

```json
{
  "screenshot": 1,
  "description": "Detailed controller description",
  "author": "Your name",
  "latest": {
    "versionCode": 1,
    "versionName": "1.0"
  },
  "history": []
}
```

## Device types

| ID | Device |
|---:|---|
| 0 | Phone |
| 1 | Tablet |
| 2 | Other device |

## Controller categories

| ID | Category | Description |
|---:|---|---|
| 1 | Universal | Contains basic features |
| 2 | Mods | Adapted for some mods |
| 3 | Imitate | Imitates another software's controller |
| 4 | PVP | Adapted for PVP games |
| 5 | Full keyboard | Contains a full keyboard |
| 6 | Style | Provides button styles for other controller creators |

## Adding a new category

Before requesting a new category:

1. Confirm that the category does not already exist.
2. Explain why it is needed.
3. Define its classification standard.
4. Provide examples of controllers that meet the standard.

Category entries use a structure like:

```json
{
  "id": 1,
  "lang": [
    {
      "locale": "en",
      "text": "Universal"
    },
    {
      "locale": "zh_CN",
      "text": "通用"
    }
  ]
}
```

## Translation guidelines

- Preserve the meaning of the original instructions.
- Do not translate JSON keys or internal identifiers.
- Keep all file paths, URLs, version codes, IDs, and commands unchanged unless explicitly required.
- Mark uncertain translations clearly for review.
- Do not alter ownership or licensing notices.
- Link to the original FCL-Team repository as the source of truth.

## Uploading files to this GitHub repository

### Web upload

1. Open this repository on GitHub.
2. Select **Add file → Upload files**.
3. Drag and drop the translated files or extracted folders.
4. Enter a short commit description.
5. Select **Commit changes**.

### Git upload

```bash
git clone https://github.com/Shoaib-Ur-Rahman/FCL-Controllers-Translated.git
cd FCL-Controllers-Translated
git add .
git commit -m "Update translated documentation"
git push origin main
```

## Original project and credits

- **Original project:** [FCL-Team/FCL-Controllers](https://github.com/FCL-Team/FCL-Controllers)
- **Translation maintainer:** [Shoaib-Ur-Rahman](https://github.com/Shoaib-Ur-Rahman)

All rights and credits for original project content belong to FCL-Team and the respective original authors. If there is a license or permission requirement, it applies to the corresponding original content. When in doubt, contact the original maintainers before redistribution.
