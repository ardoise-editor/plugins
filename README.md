# Ardoise Editor official plugins

`registry.json` is the list of the official plugins that
[Ardoise Editor](https://github.com/ardoise-editor/ardoise) shows in
**Preferences › Plugins**. The editor reads it from
`https://raw.githubusercontent.com/ardoise-editor/plugins/main/registry.json`.

```json
{
  "version": 1,
  "plugins": [
    {
      "id": "simpleedit.lint",
      "name": { "en": "Lint", "fr": "Lint" },
      "description": { "en": "Problems of the file as you type", "fr": "Les problèmes du fichier pendant la saisie" },
      "repository": "simple-edit-app/plugin-lint"
    }
  ]
}
```

An official plugin:

- has an id that starts with `simpleedit.` (the namespace of the official
  plugins, from before the editor was renamed: it stays), and its repository is
  in the `ardoise-editor` organization (the editor ignores any other entry).
  The entries below still say `simple-edit-app`, the former name of the
  organization: the versions of the editor from before the rename only list
  repositories under it, and GitHub sends them to the new name;
- signs the `SHA256SUMS` of its releases (`SHA256SUMS.sig`) with the key of
  the editor's own releases: the editor refuses an official plugin whose
  signature is missing or wrong.

Anyone else's plugin is installed from its repository (`owner/name`) on the
same page, after a warning. The guide to writing one:
<https://ardoise-editor.github.io/ardoise/plugins.html>.

`python3 check.py` checks the file; it runs on every push.
