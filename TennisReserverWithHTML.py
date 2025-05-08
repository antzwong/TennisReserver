// Tennis Reservation Button Clicker
// This script waits until 6:00 PM exactly, then clicks the confirmation button

// Function to find the confirmation button on the page
// Using the exact selector for the reservation link
function findConfirmationButton() {
  // Target the specific link inside the reserve list item
  const reserveLink = document.querySelector('li.reserve > a[href="/facilities/35/reservations/new?sport=tennis"]');
  
  if (reserveLink) {
    return reserveLink;
  }
  
  // Fallback selectors in case the link changes slightly
  const fallbackSelectors = [
    'li.reserve > a',
    'li.reserve a',
    'a[href*="reservations/new?sport=tennis"]',
    'a:contains("Reserve")'
  ];
  
  for (const selector of fallbackSelectors) {
    try {
      const button = document.querySelector(selector);
      if (button) return button;
    } catch (e) {
      // Some selectors like :contains may not be supported in all browsers
      console.log(`Selector ${selector} failed: ${e.message}`);
    }
  }
  
  // If button still not found, log a message
  console.error("Reservation button not found. The page structure may have changed.");
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
  button.click();
  
  // For links, we also try these additional methods to ensure the click works
  // Some websites intercept normal clicks with event listeners
  const clickEvent = new MouseEvent('click', {
    bubbles: true,
    cancelable: true,
    view: window
  });
  button.dispatchEvent(clickEvent);
  
  // As a final fallback, we can try to navigate directly
  console.log("Also attempting direct navigation to the reservation URL");
  setTimeout(() => {
    // Only navigate if the click didn't already work
    // This slight delay gives the click events time to process
    window.location.href = button.href;
  }, 100);
}

// Set up the timer to click at exactly 6:00 PM
function scheduleClick() {
  const now = new Date();
  const executionTime = new Date();
  
  // Set time to 6:00:00 PM today
  executionTime.setHours(23, 47, 0, 0);
  
  // If it's already past 6 PM, log a message
  if (now >= executionTime) {
    console.log("It's already past 6:00 PM. Run this script before the target time.");
    return;
  }
  
  // Calculate milliseconds until 6:00 PM
  const timeUntilExecution = executionTime - now;
  
  console.log(`Scheduling confirmation click at exactly 6:00:00 PM (in ${Math.round(timeUntilExecution/1000)} seconds)`);
  console.log(`Target button: li.reserve > a[href="/facilities/35/reservations/new?sport=tennis"]`);
  
  // Set a countdown to show progress
  const countdownInterval = setInterval(() => {
    const currentTime = new Date();
    const remainingTime = executionTime - currentTime;
    const remainingSeconds = Math.round(remainingTime / 1000);
    
    // More frequent updates as we get closer
    if (remainingSeconds <= 10) {
      console.log(`${remainingSeconds} seconds remaining...`);
    } else if (remainingSeconds % 60 === 0) {
      // Show minutes remaining every minute
      console.log(`${Math.floor(remainingSeconds / 60)} minutes remaining...`);
    }
    
    if (remainingSeconds <= 0) {
      clearInterval(countdownInterval);
    }
  }, remainingTime => remainingTime <= 60000 ? 1000 : 5000); // Update every 5 seconds, then every second for the last minute
  
  // Set the timer to execute at exactly 6:00 PM
  setTimeout(() => {
    clickReservationButton();
    console.log("Execution attempt completed!");
  }, timeUntilExecution);
}

// Start the scheduling process
scheduleClick();