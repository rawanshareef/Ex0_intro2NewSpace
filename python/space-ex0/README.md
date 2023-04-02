
This branch contains a solution to support 10% errors margins on statrting state.
It automatically runs all possible margins [1.0, 1.1, 0.9] on "vs", "alt", "hs", "fuel".

We treated the flight function as a function with multi variables and used scipy minimize function to find best values to satisfy conditions.
This solution also hovers vertically to cancel out any residual hs left when vertically landing.


Dont forget:  
`pip install -r requirements.txt`
