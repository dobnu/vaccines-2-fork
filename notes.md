# Changes Made to Vaccines-2-Fork
## 1. Removed gzip using filter-repo
Had to do some special stuff to be able to push back to main branch

## 2. Updates months.csv with new dates, some malfunctioned, fixed that
Hard coded start date into vaccines.py as a simple fix, because start date was also listed as an end date

Found issue with 07-31-2022
	Merge .csv blank
	JHU/deaths .csv appears fine
	Vaccinations 07-31-2022 .csv is empty

Deleted all (5) problematic dates (other option would have been to ignore bad dates, probably better?)

## 3. Set Imageio to version used originally
Issue with imageio, recommended I import imageio.v2 to keep current behavior, otherwise imageio v3 will be used
Imageio.v2 used

## 4. Fixed Order of Scatter plot gif

## 5. Used seaborn to plot deaths in two counties. Am I supposed to add the line graph?

Theory: more vaccination means delay in outbreaks, but as virus changes still see an increase in covid deaths once vaccines are not sufficiently protective against variant that is significantly different