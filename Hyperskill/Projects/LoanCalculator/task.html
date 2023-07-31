<h1>Stage 1</h1>

<p>Let's think about what a loan calculator should be able to do. In general, it takes several parameters like a loan principal and interest, calculates the values the user wants to know (for example, monthly payment or overpayment), and outputs them to the user.</p>

<p>Not familiar with these concepts? Don't worry, we will explain them to you in simple terms. The principal is the original amount of money you borrow. The interest is a charge for borrowing that money, usually calculated as a percentage of the principal amount.</p>

<p><strong>Objective</strong></p>

<p>Let's start by imitating this behavior. There are some prepared variables in the source code: these are text messages that our loan calculator can output. In this stage, all you need to do is output them in the right order.</p>

<p><strong>Example</strong></p>

<p>Output:</p>

<pre><code class="language-no-highlight">Loan principal: 1000
Month 1: repaid 250
Month 2: repaid 250
Month 3: repaid 500
The loan has been repaid!</code></pre>

<h1>Stage 2</h1>

<p>If you found the previous stage too easy, let's add something interesting. The best loans are probably those with a 0% interest.</p>

<p>Let's make some calculations for 0% loan repayments. The user might know the period of the loan and want to calculate the monthly payment. Or the user might know the amount of the monthly repayments and wonder how many months it will take to repay the loan in full. </p>

<p>In this stage, we need to ask the user to input the loan principal amount. Then, the user should indicate what needs to be calculated (the monthly payment amount or the number of months) and enter the required parameter. After that, the loan calculator should output the value that the user wants to know.</p>

<p>Also, let’s assume we don't care about decimal places. If you get a floating-point expression as a result of the calculation, you’ll have to do additional actions. Take a look at Example 4 where you need to calculate the monthly payment. You know that the loan principal is 1000 and want to pay it back in 9 months. The real value of payment can be calculated as:</p>

<p style="text-align: center;"><span class="math-tex">\(payment = \dfrac{principal}{months}=\dfrac{1000}{9} =111.11...\)</span></p>

<p>Of course, you can’t pay that amount of money. You have to round up this value and make it 112. Remember that no payment can be more than the fixed monthly payment. If your monthly repayment amount is 111, that would make the last payment 112, which is not acceptable. If you make a monthly payment of 112, the last payment will be 104, which is fine. You can calculate the last payment as follows:</p>

<p style="text-align: center;"><span class="math-tex">\(lastpayment =principal -(periods-1)*payment = 1000 - 8*112=104\)</span></p>

<p>In this stage, you need to count the number of months or the monthly payment. If the last payment differs from the rest, the program should display the monthly payment and the last payment.</p>

<p><strong>Objective</strong></p>

<p>The behavior of your program should look like this:</p>

<ul>
	<li>Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount.</li>
	<li>To perform further calculations, you'll also have to ask for the required missing value.</li>
	<li>Finally, output the results for the user.</li>
</ul>


<p><strong>Example 1</strong></p>

<pre><code class="language-no-highlight">Enter the loan principal:
&gt; 1000
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
&gt; m
Enter the monthly payment:
&gt; 150

It will take 7 months to repay the loan</code></pre>

<p><strong>Example 2</strong></p>

<pre><code class="language-no-highlight">Enter the loan principal:
&gt; 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
&gt; m
Enter the monthly payment:
&gt; 1000

It will take 1 month to repay the loan</code></pre>

<p><strong>Example 3</strong></p>

<pre><code class="language-no-highlight">Enter the loan principal:
&gt; 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
&gt; p
Enter the number of months:
&gt; 10

Your monthly payment = 100</code></pre>

<p><strong>Example 4</strong></p>

<pre><code class="language-no-highlight">Enter the loan principal:
&gt; 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment
&gt; p
Enter the number of months:
&gt; 9

Your monthly payment = 112 and the last payment = 104.</code></pre>

<h1>Stage 3</h1>

<p>Let's compute all the parameters of the loan. There are at least two kinds of loan: those with annuity payment and those with differentiated payment. In this stage, you are going to calculate only the annuity payment which is fixed during the whole loan term.</p>

<p>Here is the formula:</p>

<p style="text-align: center;"><span class="math-tex">\(A_{ordinary\_annuity} = P * \dfrac{i * (1+i)^n}{(1+i)^n-1}\)</span></p>

<p>Where:</p>

<p><span class="math-tex">\(A\)</span> = annuity payment;</p>

<p><span class="math-tex">\(P\)</span> = loan principal;</p>

<p><span class="math-tex">\(i\)</span> = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage. For example, if your annual interest rate = 12%, then i = 0.01;</p>

<p><span class="math-tex">\(n\)</span> = number of payments. This is usually the number of months in which repayments will be made.</p>

<p>You are interested in four values: the number of monthly payments required to repay the loan, the monthly payment amount, the loan principal, and the loan interest. Each of these values can be calculated if others are known:</p>

<p><strong>Loan principal:</strong></p>

<p><span class="math-tex">\(P = \dfrac{A}{\left( \dfrac{i * (1+i)^n}{(1+i)^n-1} \right)}\)</span></p>

<p><strong>The number of payments:</strong></p>

<p><strong><span class="math-tex">\(n = \log_{1+i} \left( \dfrac{A}{A - i*P} \right)\)</span></strong></p>

<p><strong>Objective</strong></p>

<p>In this stage, you should add new behavior to the calculator:</p>

<ol>
	<li>First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.</li>
	<li>Then, you need to ask them to input the remaining values.</li>
	<li>Finally, compute and output the value that they wanted.</li>
</ol>

<p><div class="alert alert-warning">Note that the user inputs the interest rate as a percentage, for example, 11.7, so you should divide this value by 100 to use it in the formula above.</div></p>

<p>Please be careful converting "<strong>X months</strong>" to "<strong>Y years and Z months</strong>". Avoid writing "0 years and 11 months" (output "11 months" instead) and "1 years and 0 months" (output "1 year" instead).</p>

<p>Note that in this stage, you have to ask the user to input parameters in a specific order which is provided below. Simply skip the value the user wants to calculate:</p>

<ul>
	<li>The first is the loan principal. </li>
	<li>The second is the monthly payment. </li>
	<li>The next is the number of monthly payments.</li>
	<li>The last is the loan interest.</li>
</ul>


<p><strong>Example 1</strong></p>

<pre><code class="language-no-highlight">What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
&gt; n
Enter the loan principal:
&gt; 1000000
Enter the monthly payment:
&gt; 15000
Enter the loan interest:
&gt; 10
It will take 8 years and 2 months to repay this loan!</code></pre>

<p>Let’s take a closer look at <strong>Example 1</strong>.</p>

<p>You know the loan principal, the loan interest and want to calculate the number of monthly payments. What do you do?</p>

<p>1) You need to know the nominal interest rate. It is calculated like this:</p>

<p><span class="math-tex">\(i = \dfrac{10\%}{12 * 100\%} = 0.008333...\)</span></p>

<p>2) Now you can calculate the number of months:</p>

<p><span class="math-tex">\(n = \log_{1 + 0.008333...} \left( \dfrac{15000}{15000-0.008333... * 1000000} \right) = 97.71...\)</span></p>

<p>3) You need an integer number, so let’s round it up. Notice that the user will pay the same amount every month for 97 months, and in the 98th month the user will pay<em> 0.71...</em> of the monthly payment. So, there are 98 months to pay.</p>

<p><span class="math-tex">\(n = 98\)</span></p>

<p>4) Finally, you need to convert “98 months” to “8 years and 2 months” so that it is more readable and understandable for the user.</p>

<p><strong>Example 2</strong></p>

<pre><code class="language-no-highlight">What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
&gt; a
Enter the loan principal:
&gt; 1000000
Enter the number of periods:
&gt; 60
Enter the loan interest:
&gt; 10
Your monthly payment = 21248!</code></pre>

<p><strong>Example 3</strong></p>

<pre><code class="language-no-highlight">What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
&gt; p
Enter the annuity payment:
&gt; 8721.8
Enter the number of periods:
&gt; 120
Enter the loan interest:
&gt; 5.6
Your loan principal = 800000!</code></pre>

<h1>Stage 4</h1>

<p>Finally, let's add to our calculator the capacity to compute differentiated payments. We’ll do this for the type of repayment where the loan principal is reduced by a constant amount each month. The rest of the monthly payment goes toward interest repayment and it is gradually reduced over the term of the loan. This means that the payment is different each month. Let’s look at the formula:</p>

<p style="text-align: center;"><span class="math-tex">\(D_m = \dfrac{P}{n} + i * \left( P - \dfrac{P*(m-1)}{n} \right) \)</span></p>

<p>Where:</p>

<p><span class="math-tex">\(D_m\)</span> = mth differentiated payment;</p>

<p><span class="math-tex">\(P\)</span> = the loan principal;</p>

<p><span class="math-tex">\(i\)</span> = nominal interest rate. This is usually 1/12 of the annual interest rate, and it’s usually a float value, not a percentage. For example, if our annual interest rate = 12%, then i = 0.01.</p>

<p><span class="math-tex">\(n\)</span> = number of payments. This is usually the number of months in which repayments will be made.</p>

<p><span class="math-tex">\(m\)</span> = current repayment month.</p>

<p>The user has to input a lot of parameters, so it might be convenient to use command-line arguments.</p>

<p>You can run your loan calculator via command line like this:</p>

<pre><code class="language-no-highlight">python creditcalc.py</code></pre>

<p>Using command-line arguments you can run your program this way:</p>

<pre><code class="language-no-highlight">python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10</code></pre>

<p>This way, your program can get different values without prompting the user to input them. It can be useful when you are developing your program and trying to find a mistake, and you want to run the program with the same parameters again and again. It's also convenient if you made a mistake in a single parameter: you don't have to input all the other values again.</p>

<p><strong>Objective</strong></p>

<p>In this stage, you are going to implement the following features:</p>

<ul>
	<li>Calculation of differentiated payments. To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.</li>
	<li>Ability to calculate the same values as in the previous stage for annuity payment (principal, number of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.</li>
	<li>Handling of invalid parameters. It's a good idea to show an error message if the user enters invalid parameters (they are discussed in detail below).</li>
</ul>

<p>The final version of your program is supposed to work from the command line and parse the following parameters:</p>

<ul>
	<li><code class="java">--type</code> indicates the type of payment: <code class="java">"annuity"</code> or <code class="java">"diff"</code> (differentiated). If <code class="java">--type</code> is specified neither as <code class="java">"annuity"</code> nor as <code class="java">"diff"</code> or not specified at all, show the error message.

	<pre><code class="language-no-highlight">&gt; python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters</code></pre>
	</li>
	<li><code class="java">--payment</code> is the monthly payment amount. For <code class="java">--type=diff</code>, the payment is different each month, so we can't calculate months or principal, therefore a combination with <code class="java">--payment</code> is invalid, too:
	<pre><code class="language-no-highlight">&gt; python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters</code></pre>
	</li>
	<li><code class="java">--principal</code> is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.</li>
	<li><code class="java">--periods</code> denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.</li>
	<li><code class="java">--interest</code> is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided. These parameters are incorrect because <code class="java">--interest</code> is missing:
	<pre><code class="language-no-highlight">&gt; python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters</code></pre>
	</li>
</ul>

<p>You may have noticed that for differentiated payments you will need 4 out of 5 parameters (excluding payment), and the same is true for annuity payments (the user will be calculating the number of payments, the payment amount, or the loan principal). Thus, you should also display an error message when fewer than four parameters are provided:</p>

<pre><code class="language-no-highlight">&gt; python creditcalc.py --type=annuity --principal=1000000 --payment=104000
Incorrect parameters</code></pre>

<p>You should also display an error message when negative values are entered:</p>

<pre><code class="language-no-highlight">&gt; python creditcalc.py --type=diff --principal=30000 --periods=-14 --interest=10
Incorrect parameters</code></pre>

<p>The only thing left is to compute the overpayment: the amount of interest paid over the whole term of the loan. Voila: you have a real loan calculator!</p>

<p><strong>Example 1: </strong><em>calculating differentiated payments</em></p>

<pre><code class="language-no-highlight">&gt; python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834

Overpayment = 45837</code></pre>

<p>In this example, the user wants to take a loan with differentiated payments. You know the principal, the count of periods, and interest, which are 1,000,000, 10 months, and 10%, respectively.</p>

<p>The calculator should calculate payments for all 10 months. Let’s look at the formula above. In this case:</p>

<p><span class="math-tex">\(P = 1000000\)</span><br>
<span class="math-tex">\(n = 10\)</span><br>
<span class="math-tex">\(i = \dfrac{ interest }{ 12 * 100\% } = \dfrac { 10\% }{12 * 100\% } = 0.008333...\)</span></p>

<p>Now let’s calculate the payment for the first month:</p>

<p><span class="math-tex">\(D_1 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(1-1) }{ 10 } \right) = 108333.333...\)</span></p>

<p>The second month (<span class="math-tex">\(m = 2\)</span>):</p>

<p><span class="math-tex">\(D_2 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(2-1) }{ 10 } \right) = 107500\)</span></p>

<p>The third month (<span class="math-tex">\(m = 3\)</span>):</p>

<p><span class="math-tex">\(D_3 = \dfrac{P}{n} + i * \left(P - \dfrac{ P * (m-1) }{ n } \right)=\dfrac{ 1000000 }{ 10 } + 0.008333... * \left( 1000000 - \dfrac{ 1000000*(3-1) }{ 10 } \right) = 106666.666...\)</span></p>

<p>And so on. You can see other monthly payments above.</p>

<p><div class="alert alert-warning">Your loan calculator should output monthly payments for every month as in the first stage. Also, round up all floating-point values.</div></p>

<p>Finally, your loan calculator should add up all the payments and subtract the loan principal so that you get the overpayment.</p>

<p><strong>Example 2: </strong><em>calculate the annuity payment for a 60-month (5-year) loan with a principal amount of 1,000,000 at 10% interest</em></p>

<pre><code class="language-no-highlight">&gt; python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880</code></pre>

<p><strong>Example 3: </strong><em>fewer than four arguments are given</em></p>

<pre><code class="language-no-highlight">&gt; python creditcalc.py --type=diff --principal=1000000 --payment=104000
Incorrect parameters.</code></pre>

<p><strong>Example 4: </strong><em>calculate differentiated payments given a principal of 500,000 over 8 months at an interest rate of 7.8%</em></p>

<pre><code class="language-no-highlight">&gt; python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
Month 1: payment is 65750
Month 2: payment is 65344
Month 3: payment is 64938
Month 4: payment is 64532
Month 5: payment is 64125
Month 6: payment is 63719
Month 7: payment is 63313
Month 8: payment is 62907

Overpayment = 14628</code></pre>

<p><strong>Example 5: </strong><em>calculate the principal for a user paying 8,722 per month for 120 months (10 years) at 5.6% interest</em></p>

<pre><code class="language-no-highlight">&gt; python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your loan principal = 800018!
Overpayment = 246622</code></pre>

<p><strong>Example 6: </strong><em>calculate how long it will take to repay a loan with 500,000 principal, monthly payment of 23,000, and 7.8% interest</em></p>

<pre><code class="language-no-highlight">&gt; python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!
Overpayment = 52000</code></pre>