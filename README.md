# WP_plugin_ratings_scraper
A short script for getting the ratings of all WordPress plugins, listed on api.wordpress.org/plugins, that have any specified tag

## The problem
I wanted to create a simple script for the purpose of creating an Excel table of the amount and average ratings of WordPress plugins tagged with performance optimization related any related tag such as "optimization".

##Solution
By utilizing the [WordPress.org API](https://codex.wordpress.org/WordPress.org_API), I created a script that fetches plugins that have the specified tag and writes the name of the plugin along with its numerical rating (0-100)
