# billionaire-model

A model to calculate how long it will take before the rich own every worldly saleable asset.


doc render samples remove when complete.
```math
\left. {\frac{a_1}{a_2}} \middle/ {\frac{b_1}{b_2}} \right.
```

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
  
2. Mathematical Formulation

    Let:

    - $W(t)$ = total world wealth at year $t$.
    - $w(t)$ = combined wealth of the billionaire group at year $t$.

Growth equations (assuming discrete annual compounding):
```math
  W(t) = W0 ⋅ (1 + g)^t,
```

```math
  w(t) = w0 ⋅ (1 + r)^t.
```
 
We define the fraction of total wealth held by the billionaires at time $t$ as:

```math
  f(t)  = {\frac{w(t)}{W(t)}}.
```

Substituting the expressions above into $f(t)$:

```math
f(t) \;=\; \frac{w(t)}{W(t)}
       \;=\;
       \frac{w_0 \,(1 + r)^t}{W_0 \,(1 + g)^t}
       \;=\;
       \frac{w_0}{W_0}
       \left(\frac{1 + r}{1 + g}\right)^t.
```

Let

```math
f0 = \frac{w0}{W0}
```

be the fraction of wealth the billionaires start out with. If $f0$ is small (e.g., 2%, 5%, etc.), it means the rest of the world holds the majority at $t = 0.$


We want to find $t$ such that $f(t) = 1$, i.e., the billionaires own 100%:

```math
f0 (1+r 1+g)t = 1.
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

3. Example Calculation

Suppose (all numbers are purely illustrative):

- Total world wealth, $W0 = 450$ trillion USD.
- Billionaires’ combined wealth, $w0 = 10$ trillion USD.
  &nbsp;&nbsp; ⇒ So they start with about $f0 = 10/450 = 0.022$, or 2.2% of all wealth.
- Global annual wealth growth rate, $g = 3%$ (i.e., the total pie grows 3% per year).
- Billionaires’ annual growth rate, $r = 15%$
  
We plug into our formula:

```math
f0 = 0.22, 
frac{1 + r}{1 + g} = \frac{1.15}{1.03} \approx 1.126,

\quad
t = \frac{\ln(1 / 0.022)}{\ln(1.126)}

\approx 31.8 \;\text{years}.
```
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


\section{Key Assumptions}
\begin{itemize}
  \item \textbf{Initial total wealth (worldwide):} \(W_0\). \\
    This is the sum of all assets in the world at the starting point \(t = 0\).
  \item \textbf{Initial combined wealth of the billionaire group:} \(w_0\). \\
    This is the sum of the net worth of the small set of wealthiest individuals at \(t = 0\).
  \item \textbf{Annual growth rate of total world wealth:} \(g\). \\
    The rate at which global wealth grows each year (e.g., 3\%).
  \item \textbf{Annual growth rate of the billionaire group’s wealth:} \(r\). \\
    The rate at which the billionaires’ collective wealth grows each year (e.g., 15\%).
  \item \textbf{No “leakage” outside the system.} \\
    We assume wealth transfers stay within the same closed economic system.
  \item \textbf{Aim:} \\
    Determine how many years it takes for the billionaires to own essentially all assets.
\end{itemize}

\section{Mathematical Formulation}
Let \(W(t)\) be the total world wealth at year \(t\) and \(w(t)\) be the billionaires' combined wealth at year \(t\). We assume discrete annual compounding:
\[
W(t) \;=\; W_0 \,(1 + g)^t,
\quad
w(t) \;=\; w_0 \,(1 + r)^t.
\]
Define the fraction of total wealth owned by the billionaires at time \(t\) as
\[
f(t) \;=\; \frac{w(t)}{W(t)}
       \;=\;
       \frac{w_0 \,(1 + r)^t}{W_0 \,(1 + g)^t}
       \;=\;
       \frac{w_0}{W_0}
       \left(\frac{1 + r}{1 + g}\right)^t.
\]
Let \(f_0 = \tfrac{w_0}{W_0}\) be their initial share of total wealth. We seek \(t\) such that \(f(t) = 1\), i.e.\ full ownership:
\[
f_0 \left(\frac{1 + r}{1 + g}\right)^t
= 1
\quad \Longrightarrow \quad
t
= \frac{\ln\!\bigl(\tfrac{1}{f_0}\bigr)}{
   \ln\!\Bigl(\tfrac{1 + r}{1 + g}\Bigr)}.
\]

\section{Example Calculation}
Suppose:
\begin{itemize}
  \item \(W_0 = 450\,\text{trillion USD}\)
  \item \(w_0 = 10\,\text{trillion USD}\) \quad(\(\Rightarrow f_0 = 10/450 = 0.022\))
  \item \(g = 3\%\)
  \item \(r = 15\%\)
\end{itemize}
Then
\[
\frac{1 + r}{1 + g} = \frac{1.15}{1.03} \approx 1.126,
\quad
t
= \frac{\ln(1 / 0.022)}{\ln(1.126)}
\approx 31.8 \;\text{years}.
\]
Hence, under these assumptions, it takes around 32 years for the billionaires’ share to approach 100\%.

\section{Caveats and Real-World Complexity}
\begin{itemize}
  \item \textbf{Changing membership:} The set of the wealthiest individuals is not static.
  \item \textbf{Varying rates of return:} Not all investments grow at a constant rate; market fluctuations occur.
  \item \textbf{Taxes and redistribution:} Real economies have taxation, philanthropy, and other factors that complicate wealth accumulation.
  \item \textbf{Innovation and new wealth creation:} New technologies can create new billionaires or redistribute wealth in unpredictable ways.
  \item \textbf{Spending vs.\ reinvesting:} Ultra-rich individuals do not necessarily reinvest everything at the same rate.
\end{itemize}

\section{Summary of the Model}
\begin{itemize}
  \item \textbf{Fraction of wealth at time \(t\):}
    \[
      f(t)
      =
      f_0 \left(\frac{1 + r}{1 + g}\right)^t.
    \]
  \item \textbf{Years until billionaires own all wealth:}
    \[
      t
      =
      \frac{\ln\!\bigl(\tfrac{1}{f_0}\bigr)}{
      \ln\!\Bigl(\frac{1 + r}{1 + g}\Bigr)}
      \quad\text{(valid if \(r > g\)).}
    \]
\end{itemize}
