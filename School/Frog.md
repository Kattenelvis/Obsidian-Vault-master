
Problemet kan översättas till ett problem i modulo aritmetik. Varje bokstav kan mappas till ett tal, där $A=1, B=2,...G=7$. Frågan kan då ekvivalent ställas om till "Vad blir resten när $2^{146}$ delas på 7?". 

Notera att $2^6 \equiv_{7}1$ vilket innebär att $2^{146}= 2^{6⋅24+2}=(2^6)^{24}2^2\equiv_7 1^{24}2^2=4$. 

Alltså hamnar grodan på den fjärde rutan, eller D i figuren.







Uppgift 2


a) $A$ och $B$ separat från varandra drar $10$ linjer var till höger sida, så med $10$ möjligheter multiplicerat med $10$ möjligheter blir $10^2$ totala möjligheter. Eftersom det finns 10 konfigurationer där dom dras till samma siffra så subtraheras dom från det totala. Alltså blir det $10^2-10=90$ möjligheter.

b) Jag antar att om $A$ och $B$ går till samma siffra så korsar det varandra. Då för $B$ mappas till $n$ så finns det $n-1$ möjliga mappningar för $A$. Så t.ex om B är $3$ så finns det $2$ konfigurationer. Alltså blir det totala antalet konfigurationer där linjerna ej korsar $1+2+...+9=45$. 

Man kan även lösa det på följande sätt: Då det finns $2$ linjer som kartläggs till $10$ siffror där ordning spelar roll och där det inte finns någon överlap så blir det $\binom{10}{2}=45$ möjliga konfigurationer.

c) Då det finns 4 linjer som kartläggs till 10 siffror där ordning spelar roll och där det inte finns någon överlap blir det $\binom{10}{4}=210$ konfigurationer. 





D har fritt 10 möjligheter

Precis som förut, C och D har 55 möjligheter

Dela med 4 faktorial för att det finns bara en konfiguration med deras ordning


10!/2!(8!)

10\*9/2

5\*9


10!/4!(6!)

10 9 8 7
4 3 2

5 3 2 7

210

så 220





$$\begin{array}{c} A \\ B \\ C \\ D \end{array} \qquad\qquad \qquad \begin{array}{c} 1 \\ 2 \\ \vdots \\ 10 \end{array}$$
p






uppgift 3


a) $$sin(-\frac{5\pi x}{6})$$
b) $h(3)=sin(-\frac{5\pi 3}{6})=sin(-\frac{5\pi}{2})=-sin(\frac{5\pi}{2})=-1$

 $h(4)=sin(-\frac{5\pi 4}{6})=sin(-\frac{10\pi}{3})=-sin(\frac{10\pi}{3})=\frac{\sqrt{3}}{2}$

 $h(5)=sin(-\frac{5\pi 5}{6})=sin(-\frac{25\pi}{6})=-sin(\frac{\pi}{6})=-\frac{1}{2}$

c) Då komposition av definitionsmängder är transitivt, och då $g$ evalueras först, så får vi att definitionsmängden är $\mathbb{N}$. $f$ evalueras efter det, och då målmängden av $f$ är $\mathbb{R}$ 

d) Värdemängden är inte $\mathbb{R}$ då sin funktionen utan amplitud endast returnerar tal mellan -1 och 1. Dessutom så är funktionen cyklisk så endast ett ändlig delmängd av intervallen tas an som värdemängden. Varje ökning av $2\pi$ så roterar allting 360 grader, alltså varje gång $x$ är delbart med 12. Så då får vi en ändlig delmängd av dom värden funktionen tar an mellan $x=0$ och $x=11$ 



e) Flera medlemmar i definitionsmängden av $h$ kan mappas till samma värde i värdemängden. Exempel: 0, 6 

$$sin(-\frac{5\pi 0}{6})=sin(0)=0$$
$$sin(-\frac{5\pi 6}{6})=sin(-5\pi)=0$$


Alltså är $h$ inte injektiv.

f) Då $h$ är cyclisk så kommer det alltid finnas flera tal i värdemängden som aldrig kommer nås, alltså är $h$ inte surjektiv. 


