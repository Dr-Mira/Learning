<html><body>

<h1>Stage 1</h1>

<p>Digital personal assistants help people to drive cars, plan their day, buy something online. In a sense, they are simplified versions of artificial intelligence with whom you can talk.</p>
<p>In this project, you will develop step by step a simple bot that will help you study programming.</p>
<p><strong>Objective</strong></p>
<p>For the first stage, you will write a bot who displays a greeting, its name, and the date of its creation. First impressions count!</p>
<p>Your program should print the following lines:</p>
<pre><code class="language-no-highlight">Hello! My name is {bot_name}.
I was created in {birth_year}.</code></pre>
<p>Instead of <code class="java">{bot_name}</code>, print any name you choose and replace <code class="java">{birth_year}</code> with the current year (four digits).</p>
<p><strong>Example</strong></p>
<p>Output:</p>
<pre><code class="language-no-highlight">Hello! My name is Aid.
I was created in 2020.</code></pre>
<p>You can change the text if you want but print exactly two lines.</p>
<p>Next, we will use <strong>Aid</strong> and <strong>2020</strong> as your bot's name and its birth year, but you can change it if you need to.</p></body></html>


<h1>Stage 2</h1>
<p>The greeting part is great, but chatbots are also supposed to interact with a user. It's time to implement this functionality.</p>
<p><strong>Objective</strong></p>

<p>At this stage, you will introduce yourself to the bot so that it can greet you by your name.</p>
<p>Your program should print the following lines:</p>
<pre><code class="language-no-highlight">Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
What a great name you have, {your_name}!</code></pre>
<p>You may change the name and the creation year of your bot if you want.</p>
<p>Instead of <code class="java">{your_name}</code>, the bot must print your name entered from the standard input.</p>

<p><strong>Example 1:</strong> <em>a dialogue with the bot</em></p>
<pre><code class="language-no-highlight">Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
&gt; Max
What a great name you have, Max!</code></pre>
<p>Use the provided template to simplify your work. You can change the text, but not the number of printed lines.</p></body></html>

<h1>Stage 3</h1>
<p>Keep improving your bot by developing new skills for it. We suggest a simple guessing game that will predict the age of a user.</p>
<p>It's based on a simple math trick. First, take a look at this formula:</p>
<pre><code class="java">age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105</code></pre>
<p>The numbers<code class="java">remainder3</code>, <code class="java">remainder5</code> and <code class="java">remainder7</code> are the remainders of division by 3, 5 and 7 respectively.</p>
<p>It turns out that for each number ranging from <em>0</em> to <em>104</em> the calculation will result in the number itself. This perfectly fits the ordinary age range, doesn't it? Ask a user for the remainders and use them to guess the age!</p>
<p><strong>Objective</strong></p>
<p>At this stage, you will introduce yourself to the bot. It will greet you by your name and then try to guess your age using arithmetic operations.</p>
<p>Your program should print the following lines:</p>
<pre><code class="language-no-highlight">Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
Your age is {your_age}; that's a good time to start programming!</code></pre>
<p>Read three numbers from the standard input. Assume that all the numbers will be given on separate lines.</p>
<p>Instead of <code class="java">{your_age}</code>, the bot will print the age determined according to the special formula discussed above.</p>

<p><strong>Example 1:</strong> <em>a dialogue with the bot</em></p>
<pre><code class="language-no-highlight">Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
&gt; Max
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
&gt; 1
&gt; 2
&gt; 1
Your age is 22; that's a good time to start programming!</code></pre>
<p>Use the provided template to simplify your work. You can change the text, but not the number of printed lines.</p></body></html>


<h1>Stage 4</h1>
<p>Now you will teach your bot to count. It's going to become an expert in numbers!</p>
<p><strong>Objective</strong></p>
<p>At this stage, you will program the bot to count from 0 to any positive number users enter.</p>

<p><strong>Example 1:</strong> <em>a dialogue with the new version of the bot</em></p>
<pre><code class="language-no-highlight">Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
&gt; Max
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
&gt; 1
&gt; 2
&gt; 1
Your age is 22; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
&gt; 5
0 !
1 !
2 !
3 !
4 !
5 !
Completed, have a nice day!</code></pre>
<p><strong>Note: </strong>each number starts with a new line, and after a number, the bot should print the exclamation mark.</p>
<p>Use the provided template to simplify your work. You can change the text if you want, but be especially careful when counting numbers.</p></body></html>

<h1>Stage 5</h1>
<p>At the final stage, you will improve your simple bot so that it can give you a test and check your answers. The test should be a multiple-choice quiz about programming. Your bot has to repeat the test until you answer correctly and congratulate you upon completion.</p>
<p><strong>Objective</strong></p>
<p>Your bot can ask anything you want, but there are two rules for your output:</p>
<ul>
<li>the line with the test should end with the question mark character;</li>
<li>an option starts with a digit followed by the dot (<code class="java">1.</code>, <code class="java">2.</code>, <code class="java">3.</code>, <code class="java">4.</code>)</li>
</ul>
<p>If a user enters an incorrect answer, the bot may print a message:</p>
<pre><code class="language-no-highlight">Please, try again.</code></pre>
<p>The program should stop on the correct answer and print <code class="java">Congratulations, have a nice day!</code><strong> </strong>at the end.</p>

<p><strong>Example 1:</strong> <em>a dialogue with the final version of your bot</em></p>
<pre><code class="language-no-highlight">Hello! My name is Aid.
I was created in 2020.
Please, remind me your name.
&gt; Max
What a great name you have, Max!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
&gt; 1
&gt; 2
&gt; 1
Your age is 22; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
&gt; 3
0 !
1 !
2 !
3 !
Let's test your programming knowledge.
Why do we use methods?
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.
&gt; 4
Please, try again.
&gt; 2
Congratulations, have a nice day!</code></pre>
<p>The program must end with the <code class="java">Congratulations, have a nice day!</code><strong> </strong>message.</p>
<p>Use the provided template to simplify your work. You can change the text if you want. Please note that we use functions to make it easy to understand the program and add new code to it or edit later.</p></body></html>