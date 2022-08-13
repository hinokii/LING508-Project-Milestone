# Use Cases:

**1. Part Of Speech (POS) – the app takes a sentence in Japanese or Korean, and returns a single morpheme and the POS in English for each word.**
	
	Example 1: Input = 나는 열심히 공부한다. 

               Output = (나, Noun), (는, Josa*), (열심히, Adverb), (공부, Noun), (하다, Verb).

                       * Josa means postpositional particle. 
                       
**2. Translation from Japanese or Korean to English – the app takes a word or a sentence in Japanese or Korean as input and returns a word or a sentence in English.**
       
	Example 2: Input = 旅行に行きたい!  

               Output = I want to go on a trip!

**3. Translation from Japanese to Korean or from Korean to Japanese - the app takes a word or a sentence in Japanese or Korean as input and returns a word or a sentence in Korean (if input = Japanese) or Japanese (if input = Korean).**

	Example 3: Input = 猫は基本的に、ほかの動物を捕らえて食べる肉食動物です

               Output = 고양이는 기본적으로 다른 동물을 잡고 먹는 육식 동물입니다

**4.  Compute TFIDFs of Korean words and Japanese words (separately) in document**. 
 
          