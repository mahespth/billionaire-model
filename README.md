# billionaire-model
A model to calculate how long it will take before the rich own every worldly saleable asset.


1. Key Assumptions

Initial total wealth (worldwide): ```math
W
0
W 
0
```
​	
 
This is the sum of all assets in the world at the starting point (time 
t
=
0
t=0).
W
0
  
≈
  
(the combined wealth of everyone on Earth at 
t
=
0
).
W 
0
​	
 ≈(the combined wealth of everyone on Earth at t=0).
Initial combined wealth of the billionaire group: 
w
0
w 
0
​	
 
This is the sum of the net worth of the small set of wealthiest individuals at 
t
=
0
t=0.
Annual growth rate of the total world wealth: 
g
g
This is how fast global wealth grows each year. For example, if 
g
=
3
%
g=3%, then each year the world’s total wealth grows by about 3%.
Annual growth rate of the billionaire group’s wealth: 
r
r
This is how fast the very wealthiest see their combined net worth grow each year.
Because of their ability to invest in highly profitable ventures—or simply accumulate at a rate faster than the average—this rate might be higher than 
g
g.
No “leakage” outside the system:
We assume everything is happening within one closed economic system. In other words, if billionaires buy up an asset from someone else, that wealth is transferred to them. If the overall pie is growing, it grows at rate 
g
g.
Aim:
We want to find the year 
t
t at which the billionaires own all assets—i.e., when their fraction of total wealth reaches 100%.
2. Mathematical Formulation

Let:

W
(
t
)
W(t) = total world wealth at year 
t
t.
w
(
t
)
w(t) = combined wealth of the billionaire group at year 
t
t.
Growth equations (assuming discrete annual compounding):

W
(
t
)
=
W
0
⋅
(
1
+
g
)
 
t
,
w
(
t
)
=
w
0
⋅
(
1
+
r
)
 
t
.
 
W(t)
w(t)
​	
  
=W 
0
​	
 ⋅(1+g) 
t
 ,
=w 
0
​	
 ⋅(1+r) 
t
 .
​	
 
We define the fraction of total wealth held by the billionaires at time 
t
t as:

f
(
t
)
  
=
  
w
(
t
)
W
(
t
)
.
f(t)= 
W(t)
w(t)
​	
 .
Substituting the expressions above into 
f
(
t
)
f(t):

f
(
t
)
  
=
  
w
0
⋅
(
1
+
r
)
t
W
0
⋅
(
1
+
g
)
t
  
=
  
w
0
W
0
  
×
  
(
1
+
r
1
+
g
)
t
.
f(t)= 
W 
0
​	
 ⋅(1+g) 
t
 
w 
0
​	
 ⋅(1+r) 
t
 
​	
 = 
W 
0
​	
 
w 
0
​	
 
​	
 ×( 
1+g
1+r
​	
 ) 
t
 .
Let

f
0
  
=
  
w
0
W
0
f 
0
​	
 = 
W 
0
​	
 
w 
0
​	
 
​	
 
be the fraction of wealth the billionaires start out with. If 
f
0
f 
0
​	
  is small (e.g., 2%, 5%, etc.), it means the rest of the world holds the majority at 
t
=
0
t=0.

We want to find 
t
t such that 
f
(
t
)
=
1
f(t)=1, i.e., the billionaires own 100%:

f
0
 
(
1
+
r
1
+
g
)
 
t
  
=
  
1.
f 
0
​	
 ( 
1+g
1+r
​	
 ) 
t
 =1.
Rearranging for 
t
t:

(
1
+
r
1
+
g
)
t
=
1
f
0
⟹
t
=
ln
⁡
 ⁣
(
1
f
0
)
ln
⁡
 ⁣
(
1
+
r
1
+
g
)
.
( 
1+g
1+r
​	
 ) 
t
 = 
f 
0
​	
 
1
​	
 ⟹t= 
ln( 
1+g
1+r
​	
 )
ln( 
f 
0
​	
 
1
​	
 )
​	
 .
This simple formula gives you the number of years it takes (under these assumptions) for the richest group to go from owning fraction 
```math
f
0
f 
0
​	
  of total wealth to owning 100%.

3. Example Calculation

Suppose (all numbers are purely illustrative):

Total world wealth, 
W
0
=
450
W 
0
​	
 =450 trillion USD.
Billionaires’ combined wealth, 
w
0
=
10
w 
0
​	
 =10 trillion USD.
  
  
⇒
⇒ So they start with about 
f
0
=
10
/
450
=
0.022
f 
0
​	
 =10/450=0.022, or 2.2% of all wealth.
Global annual wealth growth rate, 
g
=
3
%
g=3% (i.e., the total pie grows 3% per year).
Billionaires’ annual growth rate, 
r
=
15
%
r=15%.
We plug into our formula:

f
0
=
0.022
,
1
+
r
1
+
g
  
=
  
1
+
0.15
1
+
0.03
  
=
  
1.15
1.03
  
≈
  
1.126.
f 
0
​	
 =0.022, 
1+g
1+r
​	
 = 
1+0.03
1+0.15
​	
 = 
1.03
1.15
​	
 ≈1.126.
t
  
=
  
ln
⁡
 ⁣
(
1
/
0.022
)
ln
⁡
(
1.126
)
  
=
  
ln
⁡
(
45.45
)
ln
⁡
(
1.126
)
.
t= 
ln(1.126)
ln(1/0.022)
​	
 = 
ln(1.126)
ln(45.45)
​	
 .
ln
⁡
(
45.45
)
≈
3.82
ln(45.45)≈3.82,
ln
⁡
(
1.126
)
≈
0.12
ln(1.126)≈0.12.
Hence,

t
  
≈
  
3.82
0.12
  
≈
  
31.8
  
years
.
t≈ 
0.12
3.82
​	
 ≈31.8years.
Interpretation: In this (very rough) scenario, it would take on the order of 30–32 years for that billionaire group to go from owning 2% of global assets to owning basically all of it—assuming:

15% annual growth for them,
3% for the overall pie, and
no other “leakage,” regulations, or redistributions interfering.
4. Caveats and Real‐World Complexity

Changing membership: The set of the “richest people” is not static. People die, donate, or get replaced by new fortunes.
Varying rates of return: Even ultra‐rich individuals see periods of lower growth or losses. Meanwhile, the broader economy might have recessions or booms.
Government policies, taxes, redistribution: Real economies have taxes, philanthropy, structural changes, etc., which can slow or alter wealth‐accumulation patterns.
Innovation and new wealth creation: Sometimes new technologies (e.g., AI, biotech) create new billionaires or shift the balance of wealth in unpredictable ways.
Spending vs. reinvesting: Not all billionaire assets are continually reinvested at the same rate. Some capital just sits. Some is spent on mega‐yachts or philanthropic endeavors.
Hence, this simple exponential model should not be taken as a prediction that “the rich definitely will own everything by year XXXX.” It is, however, a transparent way to see how differing growth rates can, if sustained, produce extreme wealth‐ownership concentrations over time.

5. Summary of the Model

Fraction of wealth at time 
```math
t
t:
f
(
t
)
=
f
0
 
(
1
+
r
1
+
g
)
 
t
.
f(t)=f 
0
​	
 ( 
1+g
1+r
​	
 ) 
t
 .
```


Years until the richest own it all (i.e., 
```math
f
(
t
)
=
1
f(t)=1):
t
=
ln
⁡
 ⁣
(
1
f
0
)
ln
⁡
 ⁣
(
1
+
r
1
+
g
)
(valid if 
r
>
g
).
t= 
ln( 
1+g
1+r
​	
 )
ln( 
f 
0
​	
 
1
​	
 )
​	
 (valid if r>g).
```
That single formula is the core of the “time to total ownership” calculation under the stated assumptions.
