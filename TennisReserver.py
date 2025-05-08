// Tennis Reservation Button Clicker
// This script waits until 6:00 PM exactly, then clicks the confirmation button

// Function to find the confirmation button on the page
// You may need to adjust this selector to match your specific website
function findConfirmationButton() {
  // Try common button selectors - adjust these based on your website's structure
  const possibleSelectors = [
    'button[type="submit"]',
    'input[type="submit"]',
    'button.confirm-reservation',
    'button:contains("Confirm")',
    'button:contains("Reserve")',
    '.confirmation-button',
    '#confirmButton'
  ];
  
  for (const selector of possibleSelectors) {
    const button = document.querySelector(selector);
    if (button) return button;
  }
  
  // If none of the common selectors work, log a message
  console.error("Confirmation button not found. You may need to adjust the selector.");
  return null;
}

// Function to click the button when the time comes
function clickReservationButton() {
  const button = findConfirmationButton();
  
  if (!button) {
    console.error("Could not find the confirmation button.");
    return;
  }
  
  // Check if button is disabled
  if (button.disabled || button.classList.contains('disabled')) {
    console.log("Button seems to be disabled. Attempting to click anyway...");
  }
  
  // Click the button
  console.log("Clicking reservation confirmation button!");
  console.log(button)
  button.click();
  
  // Some websites might need a more direct approach if the above doesn't work
  // Uncomment these lines if needed:
  // const clickEvent = new MouseEvent('click', {
  //   bubbles: true,
  //   cancelable: true,
  //   view: window
  // });
  // button.dispatchEvent(clickEvent);
}

// Set up the timer to click at exactly 6:00 PM
function scheduleClick() {
  const now = new Date();
  const executionTime = new Date();
  
  // Set time to 6:00:00 PM today
  // executionTime.setHours(18, 0, 0, 0);

    // Set time to 11:30:00 PM today
  executionTime.setHours(23, 35, 0, 0);
  
  // If it's already past 6 PM, log a message
  if (now >= executionTime) {
    console.log("It's already past 6:00 PM. Run this script before the target time.");
    return;
  }
  
  // Calculate milliseconds until 6:00 PM
  const timeUntilExecution = executionTime - now;
  
  console.log(`Scheduling confirmation click at exactly 6:00:00 PM (in ${Math.round(timeUntilExecution/1000)} seconds)`);
  
  // Set a countdown to show progress
  const countdownInterval = setInterval(() => {
    const currentTime = new Date();
    const remainingTime = executionTime - currentTime;
    const remainingSeconds = Math.round(remainingTime / 1000);
    
    if (remainingSeconds <= 60) {
      console.log(`${remainingSeconds} seconds remaining...`);
    }
    
    if (remainingSeconds <= 0) {
      clearInterval(countdownInterval);
    }
  }, 5000); // Update every 5 seconds, then every second for the last minute
  // Set the timer to execute at exactly 6:00 PM
  setTimeout(() => {
    clickReservationButton();
    console.log("Execution attempt completed!");
  }, timeUntilExecution);
}

// Start the scheduling process
scheduleClick();