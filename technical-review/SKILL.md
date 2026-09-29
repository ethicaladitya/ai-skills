---
name: technical-review
description: Review technical writing (blog posts, docs, runbooks, answers) as a hostile senior sysadmin before it is published, by checking every command, flag, code snippet and tool claim against the real tool or official docs. Use before publishing anything with commands or code.
---

# Technical review

AI-written technical content fails in predictable places. Check each one against reality, not memory.

## The pass
Make a list of every command, flag, field name, code snippet and factual claim about a tool. Then:

| Item | How to verify |
|---|---|
| WP-CLI command | `wp help <command> <subcommand>` on a real install: exact flags, required args, field names |
| Linux command | `man <cmd>` or `<cmd> --help` on the target OS (Ubuntu tools on an Ubuntu host) |
| PHP snippet | save it, `php -l file.php`; then read return types and every error path |
| Shell snippet | `bash -n script.sh`; check quoting, `set -e` interactions, destructive defaults |
| JS / Python | run it or at least parse it (`node --check`, `python3 -m py_compile`) |
| API behaviour | the vendor's official docs, fetched today; note the date |
| Version-specific claim | name the version, or remove the claim |

Fix every issue, then re-read the fixed parts: fixes introduce new errors.

## Error classes found in real drafts (all from top models, blind test 2026-09-29)
- **Missing required argument:** `wp user session destroy --all` needs a user (`wp user session destroy <user> --all`).
- **Wrong field name:** `wp user list --fields=registered` should be `user_registered`.
- **Broken flag syntax:** a space after a comma in `--fields=a,b, c` splits the argument.
- **Overclaiming a flag:** `wp core verify-checksums --include-root` reports extra root files; it does not verify `wp-config.php`.
- **Unsafe default in a cleanup guide:** `wp core download --force` without `--version` can silently upgrade; `wp plugin install --force --activate` activates possibly compromised code; evidence collection without `--skip-plugins --skip-themes` runs malicious code.
- **Type errors:** a PHP function declared `: array` that returns `WP_Error` on failure paths.
- **API misreads:** caching responses without checking `finishReason`; claiming an API key must go in the URL when a header is supported.
- **Incomplete fixes:** mentioning IPv6 without giving the `ip6tables` / `ip6 daddr` rule; warning about rule order without the `-I OUTPUT 1` fix.

## Output
A short list: issue → fix → how you verified it. Count them; publishers log the count.
