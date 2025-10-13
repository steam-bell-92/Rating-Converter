function convertRating() {
    const platform = document.getElementById("platform").value;
    const inputRating = parseFloat(document.getElementById("rating").value);
    const resultDiv = document.getElementById("result");

    if (isNaN(inputRating)) {
        resultDiv.textContent = "Please enter a valid number for the rating.";
        return;
    }

    let predicted = 0;
    let title = "";
    let targetPlatform = "";
    let displayRating = 0;

    // For Codeforces ratings
    function getCodeforcesTitle(rating) {
        if (rating <= 999) return "Newbie";
        else if (rating <= 1199) return "Pupil";
        else if (rating <= 1399) return "Apprentice";
        else if (rating <= 1599) return "Specialist";
        else if (rating <= 1799) return "Expert";
        else if (rating <= 1999) return "Candidate Master";
        else if (rating <= 2199) return "Master";
        else if (rating <= 2399) return "International Master";
        else if (rating <= 2699) return "Grandmaster";
        else if (rating <= 2999) return "International Grandmaster";
        else return "Legendary Grandmaster";
    }

    // For CodeChef ratings (stars)
    function getCodeChefTitle(rating) {
        if (rating <= 1399) return "1 star";
        else if (rating <= 1599) return "2 star";
        else if (rating <= 1799) return "3 star";
        else if (rating <= 1999) return "4 star";
        else if (rating <= 2199) return "5 star";
        else if (rating <= 2499) return "6 star";
        else return "7 star";
    }

    // --- Conversion Logic ---

    if (platform === "codechef") {
        // Convert CodeChef rating to Codeforces rating
        predicted = 0.9159582102199609 * inputRating - 185.00024447800962;
        targetPlatform = "Codeforces";
        title = getCodeforcesTitle(predicted);

    } else {
        // Convert Codeforces rating to CodeChef rating
        predicted = (inputRating + 185.00024447800962) / 0.9159582102199609;
        targetPlatform = "CodeChef";
        title = getCodeChefTitle(predicted);
    }

    // Round the predicted rating to the nearest whole number
    displayRating = Math.round(predicted);

    // --- Final Output (Sets the result text only once) ---
    if (displayRating < 0) {
        // Handle the edge case where the formula produces a negative rating
        resultDiv.textContent = `Predicted Rating on ${targetPlatform}: ${displayRating} (Negative rating is unexpected).`;
    } else {
        // Standard output for positive ratings
        resultDiv.textContent = `Predicted Rating on ${targetPlatform}: ${displayRating}. Your likely title is **${title}**.`;
    }
}
