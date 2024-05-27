const qus = [
    {
        question: ( "Which Nigerian held the Guiness world Cookathon record?"),
        answer: "Hilda Bacci",
    },
    {
        question: ( "Who is the current record holder for Guiness chess marathon"),
        answer: "Tunde Onukoya",
    },
    {
        question: ( "What movie is the highest grossing movie of 2024"),
        answer: "Tribe called judah"
    },
    {
        question: ( "How many nigerian music artist in recent times have won a grammy"),
        answer: "3"
    },
]

let score = 0;

qus.forEach((quiz) => {
    userAnswer = prompt(quiz.question);

    if (userAnswer.toLowerCase() === quiz.answer.toLowerCase()) {
        alert("You got that correctly");
        // console.log("You got that correctly");
        score++;
   } else { 
    // console.log("You got it wrong. Here is the right answer " + quiz.answer)
    alert("You got it wrong. Here is the right answer " + quiz.answer);
     }
 })
// console.log("You answered " + score + " out of " + qus.length + " questions correctly");
alert("You answered " + score + " out of " + qus.length + " questions correctly");

