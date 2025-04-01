# billionaire-mode

A model to calculate how long it will take before the rich own every worldly saleable asset. 


<hr>
1. Key Assumptions

- Initial total wealth (worldwide): $W^0$
​	
 
  This is the sum of all assets in the world at the starting point (time $t=0$).
   
  &nbsp;&nbsp;$W^0 ≈ $(the combined wealth of everyone on Earth at $t=0$ ).
  
- Initial combined wealth of the billionaire group: $w^0$
    This is the sum of the net worth of the small set of wealthiest individuals at $t=0$

- Annual growth rate of the total world wealth: $g$
    This is how fast global wealth grows each year. For example, if $g = 3%$, then each year the world’s total wealth grows by about 3%.

- Annual growth rate of the billionaire group’s wealth: $r$
    This is how fast the very wealthiest see their combined net worth grow each year.
    - Because of their ability to invest in highly profitable ventures—or simply accumulate at a rate faster than the average—this rate might be higher than $g$.
    
- No “leakage” outside the system:
  We assume everything is happening within one closed economic system. In other words, if billionaires buy up an asset from someone else, that wealth is transferred to them. If the overall pie is growing, it grows at rate $g$.

- Aim:
  We want to find the year $t$ at which the billionaires own all assets — i.e., when their fraction of total wealth reaches 100%.
  
<br>
<hr>
<b>2. Mathematical Formulation</b>

Let:

  - $W(t)$ = total world wealth at year $t$.
  - $w(t)$ = combined wealth of the billionaire group at year $t$.

<br>

Growth equations (assuming discrete annual compounding):
```math
  W(t) = W0 ⋅ (1 + g)^t,
```
```math
  w(t) = w0 ⋅ (1 + r)^t.
```
 
We define the fraction of total wealth held by the billionaires at time $t$ as:
<br>
<br>
```math
  f(t)  = {\frac{w(t)}{W(t)}}.
```

Substituting the expressions above into $f(t)$:

<br>



```math

f(t) \;=\; 
\frac{w_0 \,(1 + r)^t}{W_0 \,(1 + g)^t}
       \;=\;
       \frac{w_0}{W_0}
       \times
       \left(\frac{1 + r}{1 + g}\right)^t.
```

Let:

```math
f0 = \frac{w0}{W0}
```

be the fraction of wealth the billionaires start out with. If $f0$ is small (e.g., 2%, 5%, etc.), it means the rest of the world holds the majority at $t = 0.$


We want to find $t$ such that $f(t) = 1$, i.e., the billionaires own 100%:
<br>
<br>
```math
f0 \left(\frac{1 + r}{1 + g}\right)^t = 1.
```


Rearranging for $t$:
```math
\left(\frac{1 + r}{1 + g}\right)^t
= \frac{1}{f0}
\quad \Longrightarrow \quad
t
= \frac{\ln\!\bigl(\tfrac{1}{f_0}\bigr)}{
   \ln\!\Bigl(\tfrac{1 + r}{1 + g}\Bigr)}.
```

This simple formula gives you the number of years it takes (under these assumptions) for the richest group to go from owning fraction $f0$  of total wealth to owning 100%.

<hr>
3. Example Calculation

Suppose (all numbers are purely illustrative):

- Total world wealth, $W0 = 450$ trillion USD.
- Billionaires’ combined wealth, $w0 = 10$ trillion USD.
  <br>⇒ So they start with about $f0 = 10/450 = 0.022$, or 2.2% of all wealth.
- Global annual wealth growth rate, $g = 3%$ (i.e., the total pie grows 3% per year).
- Billionaires’ annual growth rate, $r = 15%$
  
We plug into our formula:

```math
f0 = 0.22, 
\frac{1 + r}{1 + g} = \frac{1+0.15}{1+0.03} \approx\frac{1.15}{1.03} \approx 1.126.
```

```math

t \approx \frac{\ln(1 / 0.022)}{\ln(1.126)} = \frac{\ln(45.45)}{\ln(1.126)}


```
```math

t \approx \frac{3.82}{0.12} \approx 31.8 \;\text{years}.

```

Interpretation: In this (very rough) scenario, it would take on the order of 30–32 years for that billionaire group to go from owning 2% of global assets to owning  all of it—assuming:

- 15% annual growth for them,

- 3% for the overall pie, and

- no other `leakage', regulations or redistributions interfering.
