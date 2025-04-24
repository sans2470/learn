-- This query shows a list of the daily top Google Search terms.


-- Problem to solve: most searched term in India, on Good friday, 18th April
SELECT
   refresh_date,
   country_code,
   term,
   rank
FROM `bigquery-public-data.google_trends.international_top_terms`


WHERE country_code = "IN"
  AND rank = 1
  AND refresh_date = "2025-04-18"


