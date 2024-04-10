
1. Formulera intervallinkapslingssatsen samt formulera och bevisa satsen om mellanliggande värden


$$\sum_{i=1}^\infty a_i\leq \sum_{i=1}^\infty b_i\leq \sum_{i=1}^\infty c_i$$
Then if the $a$ series and the $c$ series converge to some value $K$ then the $b$ series also converges to $K$. 







# Muntliga

## 1.5
![[Pasted image 20231106163405.png]]

## 1.6

En funktion är integrerar bar om gränsvärderna av en uppåtintegral och neråtintegral konvergerar till samma tal![[Pasted image 20231103215344.png]]

## 2.1 Instängning och Sammansättning

Bevis med motsats kanske funkar? Mitt egna

$f(x)\leq g(x) \leq h(x)$

$\lim f(x) = \lim h(x) = A$

Om $\lim g(x) > A$ så blir $A = \lim f(x) \leq \lim g(x)$
Om $\lim g(x) < A$ så blir $A = \lim h(x) \geq \lim g(x)$
MOTSÄGELSE!!! REEEE

Det är tal så antingen $=, <$ eller $>$ måste gälla.



Men den officiella
![[Pasted image 20231106141711.png]]
![[Pasted image 20231106141704.png]]

Sammansättningslagen
![[Pasted image 20231108150610.png]]
![[Pasted image 20231108155234.png]]


## 2.3
Om den ej har en övre begränsning, så har den ett oegentligt gränsvärde d.v.s gå mot oändligheten. Kanske idk. Följer inte från supremumaxiomet i alla fall. 

En övre begränsning av en mängd är ett tal som är större än alla andra tal i mängden. 

Supremum axiomet säger att alla icke-tomma övre begränsade mängder har ett supremum.


Om en funktion $f$ är monotont ökande och uppåt begränsad, så har den ett egentligt gränsvärde.

Bevis: Från supremum axiomet har $f$ ett supremum $S$. Vi ska visa att $lim f = S$. 

Det finns då ett tal $x_i$ sådant att $f(x_i) > S - \epsilon$ för något $\epsilon>0$. 




Antag att det är en maxpunkt $m$. Då kommer det innebära att det finns punkter runtomkring som är mindre än $m$. 
![[Pasted image 20231104104943.png]]

Med lite omskrivning blir det
$S-\epsilon - S < f(x_i) - S$
$-\epsilon<f(x_i)-S$
$\epsilon > |f(x_i)-S|$

Enligt definition av gränsvärde så blir det gött asså

Använd denna satts i 3.1 sats om mellanliggande värden

![[Pasted image 20231109120715.png]]

![[Pasted image 20231109121617.png]]
![[Pasted image 20231109121919.png]]
## 2.4
Endast om funktionen är deriverbar så är det fallet. Bevis: UHhh
Eftersom om den är deriverbar så finns det endast en unikt värde derivatan kan ta. 

Yeah yeah men det är inte relevant!
![[Pasted image 20231103221021.png]]

Om funktionen är deriverbar är den kontinuerlig. Då existerar gränsvärde. Detta kan endast vara fallet om den är 0. 

Rolles Sats (premiss för 3.5)
Först om funktionen är platt är det 0 överallt
Annars finn extrempunkt genom att tillämpa satsen om största och minsta tal. 
## 2.5
![[Pasted image 20231107110633.png]]

![[Pasted image 20231107110843.png]]
![[Pasted image 20231107110904.png]]

## 2.6

Antag att $\sum s_i$ är absolutkonvergent, så $\sum |s_i|$ är konvergent  

Vi tar att $s_i = s_i - |s_i| + |s_i|$


$\sum s_i = \sum s_i - \sum |s_i|+ \sum |s_i|$

![[Pasted image 20231108143901.png]]
![[Pasted image 20231108143937.png]]


## 3.1 sats om intervallkappsling och mellanliggande värden


intervallkappsling


![[Pasted image 20231105160640.png]]


![[Pasted image 20231105162111.png]]


![[Pasted image 20231104112133.png]]

$a$ är alltid med, och alla $x$ i $M$ är mindre än $b$.
M är uppåt begränsad och icke-tom, och har därför ett gränsvärde $\xi$ från monotonaxiomet. Bevisa att $f(\xi) = \mu$ 

Motsägelse, visa att $f(\xi) < \mu$ leder till motsägelse och vice versa. 


## 3.2

![[Pasted image 20231108204651.png]]




## 3.3

![[Pasted image 20231108205730.png]]





## 3.4 Kont funktion på [a,b] är integrerbar

Från 3.6
![[Pasted image 20231109105059.png]]
två huvudvärdessatser
$S_\_ = f(x) = S^\_$

Skiljer sig endast via en konstant via derivatkalkylens medelvärdessats

$S_\_(x) = S^\_(x) + C$

Men 
$S_\_(a) = S^\_(a)$

Så $C=0$

Därför är den integrerbar (från definitionen av integral med ett unikt integral värde)

![[Pasted image 20231109105113.png]]

## 3.5 Integralkalylens medelvärdessats

Låt $f$ vara kontinuerlig på $[a,b]$. Då finns $\xi$ så att
![[Pasted image 20231106123000.png]]
Det kan tolkas som medelvärdet av $f$!
Tänk på att det INTE är $-a$ utan $-$ står för underintegral. 


Räkneregler:
![[Pasted image 20231106123158.png]]

![[Pasted image 20231106123049.png]]


Från största-minsta satsen så är det så att
$m\leq f(x)\leq M$

![[Pasted image 20231106123451.png]]

Dom är lätta att räkna ut
![[Pasted image 20231106123559.png]]

Satsen om medelvärden innebär då att alla tal mellan det minsta och största finns med! Så då finns det ett sådan $\xi$ och är därmed bevisad. 


## 3.6

Analysens huvudsats
![[Pasted image 20231106130702.png]]

Från definitionen av derivata
![[Pasted image 20231106130718.png]]

Med denna räkneregel på vänstra integralen
![[Pasted image 20231106123158.png]]

får man
![[Pasted image 20231106130653.png]]


![[Pasted image 20231108224501.png]]

>>>>>>> 5e2048b667780950c419982ac109ac785990ff71
