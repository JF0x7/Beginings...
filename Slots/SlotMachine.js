// Add an event listener to the document that waits for the DOM to fully load
document.addEventListener('DOMContentLoaded', function() {
    // Log message to confirm that the DOM has fully loaded
    console.log("DOM fully loaded and parsed");

    // Array of emoji options to display on the reels, excluding similar-looking emojis
    var emojis = [
        "😀", "😂", "😊", "😍", "😎", "🤩", "🥳", 
        "😇", "🤯", "🥺", "🤠", "🤖", "👾", "🐱", 
        "🐶", "🦊", "🐻", "🐼", "🐨", "🦁", "🐮", 
        "🐷", "🐸", "🐵"
    ];

    // Variable to track the number of spins
    let spinCount = 0;

    // Function to randomly select an emoji with a specific bias for winning
    function getRandomEmoji(biasEmoji) {
        let winProbability;

        // Set the win probability based on the spin count
        if (spinCount === 0) {
            winProbability = 0.5; // 50% chance to win on the first spin
        } else {
            winProbability = Math.min(0.3 + 0.05 * spinCount, 1); // Increase by 5% after each spin, max 100%
        }

        // Adjust the probability to reflect the win chance
        if (Math.random() < winProbability) {
            // Return the bias emoji to increase chances of matching reels
            return biasEmoji;
        } else {
            // Randomly select an emoji from the array for diversity in outcomes
            return emojis[Math.floor(Math.random() * emojis.length)];
        }
    }

    // Function to simulate spinning reels with animations
    function spinReel(reel, duration, biasEmoji) {
        // Return a promise that resolves when the spinning completes
        return new Promise((resolve) => {
            // Calculate the number of spins based on the duration
            let spins = Math.floor(duration / 100);
            // Initialize reel spin count
            let reelSpinCount = 0;
            // Log message to indicate the start of the spin for the specified reel
            console.log(`Starting spin for ${reel.id}, duration: ${duration}`);

            // Set an interval to update the reel content at regular intervals
            let interval = setInterval(() => {
                // Update the reel with a biased random emoji
                reel.innerHTML = getRandomEmoji(biasEmoji);
                // Increment the reel spin count with each iteration
                reelSpinCount++;
                // Log the current spin count for debugging
                console.log(`Reel ${reel.id} spin count: ${reelSpinCount}`);

                // Stop spinning after the specified duration has passed
                if (reelSpinCount >= spins) {
                    // Clear the interval to stop the reel from spinning
                    clearInterval(interval);
                    // Log message to indicate the stop of the spin for the specified reel
                    console.log(`Stopping spin for ${reel.id}`);
                    // Resolve the promise to indicate the completion of the spin
                    resolve();
                }
            }, 100); // Change emoji every 100ms for a smooth spin animation
        });
    }

    // Asynchronous function to spin the slot machine
    async function spinSlotMachine() {
        // Log message to confirm the spin button was clicked
        console.log("Spin button clicked!");

        // Get references to the reel elements and result placeholder
        var reel1 = document.getElementById("reel1");
        var reel2 = document.getElementById("reel2");
        var reel3 = document.getElementById("reel3");
        var result = document.getElementById("result");

        // Clear the result text to prepare for new spin results
        result.innerHTML = "";

        // Choose a bias emoji to increase the chances of winning
        var biasEmoji = emojis[Math.floor(Math.random() * emojis.length)];

        // Spin each reel with different durations for a staggered effect
        await Promise.all([
            spinReel(reel1, 2000, biasEmoji),
            spinReel(reel2, 2500, biasEmoji),
            spinReel(reel3, 3000, biasEmoji)
        ]);

        // Check if all three reels match after spinning completes
        if (reel1.innerHTML === reel2.innerHTML && reel2.innerHTML === reel3.innerHTML) {
            // Display jackpot message if all three reels match
            result.innerHTML = "Jackpot! 🎉";
            // Reset the spin count after a win
            spinCount = 0;
        } else {
            // Display try again message if the reels do not match
            result.innerHTML = "Try Again!";
            // Increment the spin count after each spin
            spinCount++;
        }

        // Log message to indicate the completion of the spin
        console.log("Spin completed!");
    }

    // Add an event listener to the spin button to trigger the spinSlotMachine function on click
    document.getElementById("spinButton").addEventListener("click", spinSlotMachine);
});
