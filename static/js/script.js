document.addEventListener("DOMContentLoaded", function () {
    // Simulate fetching donor data from the server
    const donor = {
        name: "Anish  Joshi",
        donationAmount: 1000,
        impactMessage: "Your generosity has helped provide essential healthcare and education to those in need. Thank you!",
    };

    // Update personalized shoutout content
    const shoutoutContent = document.getElementById("shoutoutContent");
    shoutoutContent.innerHTML = `
        Dear ${donor.name},<br>
        We are immensely grateful for your generous donation of $${donor.donationAmount}.<br>
        ${donor.impactMessage}
    `;

    // You can add more dynamic content updates or interactions here as needed
});
