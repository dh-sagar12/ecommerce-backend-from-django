-- FUNCTION: product.slugify(text)

-- DROP FUNCTION product.slugify(text);

CREATE OR REPLACE FUNCTION product.slugify(
	value text)
    RETURNS text
    LANGUAGE 'sql'

    COST 100
    IMMUTABLE STRICT 
    
AS $BODY$
  -- removes accents (diacritic signs) from a given string --
  WITH "unaccented" AS (
    SELECT unaccent("value") AS "value"
  ),
  -- lowercases the string
  "lowercase" AS (
    SELECT lower("value") AS "value"
    FROM "unaccented"
  ),
  -- replaces anything that's not a letter, number, hyphen('-'), or underscore('_') with a hyphen('-')
  "hyphenated" AS (
    SELECT regexp_replace("value", '[^a-z0-9\\-_]+', '-', 'gi') AS "value"
    FROM "lowercase"
  ),
  -- trims hyphens('-') if they exist on the head or tail of the string
  "trimmed" AS (
    SELECT regexp_replace(regexp_replace("value", '\\-+$', ''), '^\\-', '') AS "value"
    FROM "hyphenated"
  )
  SELECT "value" FROM "trimmed";
$BODY$;

ALTER FUNCTION product.slugify(text)
    OWNER TO postgres;
