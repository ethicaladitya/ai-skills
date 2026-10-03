---
name: wordpress-safe-changes
description: Make changes to live WordPress sites safely and debug SEO-plugin output (Rank Math, Yoast) with WP-CLI over SSH, without editing plugin or theme files, with backups and live verification. Use when changing settings, content, meta or plugins on a production WordPress site, or when SEO tags or schema are missing.
---

# Safe changes on live WordPress

## Rules
1. **Never edit plugin or theme files.** Updates overwrite them. Customize through settings, post meta,
   a must-use plugin (`wp-content/mu-plugins/*.php`) or a child theme.
2. **Back up exactly what you change,** on the server, before changing it:
   - options: `wp option get <name> --format=json > ~/backups/<name>-$(date +%Y%m%d-%H%M).json`
   - post: `wp post get <id> --field=post_content > .../post-<id>.html` and `wp post meta list <id> --format=json`
   - plugin: `tar -czf .../<plugin>-<version>.tgz -C wp-content/plugins <plugin>`
3. **Write content with `wp eval-file`,** never `--post_content=` on the command line (quoting breaks HTML).
4. **Verify on the live site with a cache-busting query** (`?nc=<timestamp>`), parsing the real `<head>`.
5. **Log** what changed, where the backup is, and how to roll back.

## Debugging "the SEO plugin outputs nothing"
Work from the live request, not from WP-CLI (CLI runs a different code path).
1. Fetch the page and check `<head>` for the plugin comment, `<meta name="description">`, OG tags and `application/ld+json`.
2. **Check dates in `debug.log`** before blaming an error; old fatals are often not the current cause.
3. Probe a real request with a temporary, secret-gated must-use plugin, then delete it at once:
   ```php
   <?php // wp-content/mu-plugins/zz-debug.php, delete after use
   if ( ( $_GET['dbg'] ?? '' ) === 'RANDOM_SECRET' ) {
     add_action( 'wp_footer', function () {
       global $wp_filter;
       echo '<!-- DBG ' . esc_html( wp_json_encode( [
         'rank_math_head' => isset( $wp_filter['rank_math/head'] ),
         'json_ld'        => isset( $wp_filter['rank_math/json_ld'] ),
       ] ) ) . ' -->';
     }, 999 );
   }
   ```
4. Read the plugin's bootstrap for early `return`s (requirements, registration, licence gates).

## Rank Math: known traps
- **Unregistered and not skipped = no front-end output at all.** `Registration->invalid` returns before
  any hooks. Fix: `wp option update rank_math_registration_skip 1` (same as "Skip" in the wizard).
- **`rank_math_modules` must be a PHP array of slugs,** e.g. `["rich-snippet"]`. A JSON *string* silently
  disables every module (schema, sitemap, redirections).
- **Upgrade routines run on `admin_init` in wp-admin only.** From CLI, call
  `(new \RankMath\Updates())->perform_updates()` and confirm `rank_math_version` matches the plugin.
- **Static front page:** title and description come from that page's `rank_math_title` and
  `rank_math_description` meta, not the global homepage option.
- **Knowledge graph:** a business site should be `knowledgegraph_type = company`, not `person`.
- Enabling Rank Math's sitemap module replaces `/wp-sitemap.xml` with `/sitemap_index.xml`. Only do it
  if you also update robots.txt and Search Console.

## Yoast
Title `_yoast_wpseo_title`, description `_yoast_wpseo_metadesc`, focus keyword `_yoast_wpseo_focuskw`.
- **Yoast Premium 301s live in two options.** Adding to `wpseo-premium-redirects-base` alone did nothing; the front end reads `wpseo-premium-redirects-export-plain` (keyed by origin slug). Back up both, update both, purge the cache, then `curl -I` the old URL. (2026-10-03)
- **Yoast caches its sitemaps.** After publishing, call `WPSEO_Sitemaps_Cache::clear()` or the new page is missing from the sitemap. (2026-10-03)
- **Generate block-comment JSON with a JSON encoder** (escape `<`, `>`, `--`), re-parse it before upload, and check the live page's FAQ question count; hand-written JSON silently drops the FAQ block. (2026-10-03)

## Content traps
- **Never paste `<meta>` tags or JSON-LD into post content** (Custom HTML blocks). It's invalid in the
  body, and SEO plugins may use the text as the auto description. Move the values into the plugin's fields.
- After content changes on LiteSpeed hosts: `wp litespeed-purge all`, or `wp cache flush`.
