# SimpleEdit official plugins

`registry.json` is the list of the official plugins that
[SimpleEdit](https://github.com/simple-edit-app/simpleedit) shows in
**Preferences › Plugins**. The editor reads it from
`https://raw.githubusercontent.com/simple-edit-app/plugins/main/registry.json`.

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

- has an id that starts with `simpleedit.`, and its repository is in the
  `simple-edit-app` organization (the editor ignores any other entry);
- signs the `SHA256SUMS` of its releases (`SHA256SUMS.sig`) with the key of
  SimpleEdit's own releases: the editor refuses an official plugin whose
  signature is missing or wrong.

Anyone else's plugin is installed from its repository (`owner/name`) on the
same page, after a warning. The guide to writing one:
<https://simple-edit-app.github.io/simpleedit/plugins.html>.

`python3 check.py` checks the file; it runs on every push.
