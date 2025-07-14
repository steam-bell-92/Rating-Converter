function convertRating() {
    const platform = document.getElementById("platform").value;
    const inputRating = parseFloat(document.getElementById("rating").value);
    const resultDiv = document.getElementById("result");

    if (isNaN(inputRating)) {resultDiv.textContent = "Please enter a valid rating.";
        return;}

    let predicted = 0;
    
        if (platform === "codechef") {
            // Convert CodeChef to Codeforces
            predicted = 0.9159582102199609 * inputRating - 185.00024447800962;
            {resultDiv.textContent = `Predicted Rating on Codeforces: 0`;}

            function getTitle1(rating) {
                if (predicted <= 999) return "Newbie";
                else if (predicted <= 1199) return "Pupil";
                else if (predicted <= 1399) return "Apprentice";
                else if (predicted <= 1599) return "Specialist";
                else if (predicted <= 1799) return "Expert";
                else if (predicted <= 1999) return "Candidate Master";
                else if (predicted <= 2199) return "Master";
                else if (predicted <= 2399) return "International Master";
                else if (predicted <= 2699) return "Grandmaster";
                else if (predicted <= 2999) return "International Grandmaster";
                else return "Legendary Grandmaster";}
        }
        
        else {
            // Convert Codeforces to CodeChef
            predicted = (inputRating + 185.00024447800962) / 0.9159582102199609;
            {resultDiv.textContent = `Predicted Rating on Codechef: 0`;} 
            
            function getTitle2(predicted) {
                if (predicted <= 1399) return "1 star";
                else if (predicted <= 1599) return "2 star";
                else if (predicted <= 1799) return "3 star";
                else if (predicted <= 1999) return "4 star";
                else if (predicted <= 2199) return "5 star";
                else if (predicted <= 2499) return "6 star";
                else return "7 star";
            } 
        }
        if (predicted >= 0) {
            resultDiv.textContent = `You are ${(getTitle1(predicted))} with rating: ${Math.round(predicted)}`;
            resultDiv.textContent = `You are ${(getTitle2(predicted))} with rating: ${Math.round(predicted)}`;}
        else {
            resultDiv.textContent = `You are ${(getTitle1(predicted))} with rating: 0`;
            resultDiv.textContent = `You are ${(getTitle2(predicted))} with rating: 0`;}
}