// Initial mock feedbacks to showcase on first load
const DEFAULT_FEEDBACKS = [
  {
    id: "fb-1",
    name: "Aman Gupta",
    course: "B.Tech Computer Science",
    rating: 5,
    feedback: "The DevOps and Cloud Computing curriculum is very practical and informative. The hands-on lab sessions on CI/CD pipelines are great!",
    timestamp: "10 mins ago"
  },
  {
    id: "fb-2",
    name: "Pooja Verma",
    course: "B.Tech Data Science & AI",
    rating: 4,
    feedback: "Great faculty support and comprehensive study material. Would love to have more guest lectures from industry experts.",
    timestamp: "1 hour ago"
  }
];

// State Management
let feedbacks = [];

// DOM Elements
const feedbackForm = document.getElementById("feedbackForm");
const studentNameInput = document.getElementById("studentName");
const courseNameInput = document.getElementById("courseName");
const feedbackTextInput = document.getElementById("feedbackText");
const ratingButtons = document.querySelectorAll(".rating-btn");
const ratingValueInput = document.getElementById("ratingValue");
const feedbackList = document.getElementById("feedbackList");
const emptyState = document.getElementById("emptyState");
const feedbackCount = document.getElementById("feedbackCount");
const resetBtn = document.getElementById("resetBtn");
const clearAllBtn = document.getElementById("clearAllBtn");
const searchInput = document.getElementById("searchInput");
const charCount = document.getElementById("charCount");
const toast = document.getElementById("toast");

// Validation Error Elements
const nameError = document.getElementById("nameError");
const courseError = document.getElementById("courseError");
const feedbackError = document.getElementById("feedbackError");

// Initialize Application
document.addEventListener("DOMContentLoaded", () => {
  loadFeedbacks();
  setupEventListeners();
  renderFeedbacks();
});

// Load Feedbacks from LocalStorage or Defaults
function loadFeedbacks() {
  const stored = localStorage.getItem("student_feedbacks");
  if (stored) {
    try {
      feedbacks = JSON.parse(stored);
    } catch (e) {
      feedbacks = [...DEFAULT_FEEDBACKS];
    }
  } else {
    feedbacks = [...DEFAULT_FEEDBACKS];
    saveFeedbacks();
  }
}

// Save Feedbacks to LocalStorage
function saveFeedbacks() {
  localStorage.setItem("student_feedbacks", JSON.stringify(feedbacks));
}

// Setup Event Listeners
function setupEventListeners() {
  // Form Submit
  feedbackForm.addEventListener("submit", handleFormSubmit);

  // Form Reset
  resetBtn.addEventListener("click", resetForm);

  // Clear All
  clearAllBtn.addEventListener("click", handleClearAll);

  // Search Filter
  searchInput.addEventListener("input", handleSearch);

  // Character Count
  feedbackTextInput.addEventListener("input", () => {
    const len = feedbackTextInput.value.length;
    charCount.textContent = `${len} / 500`;
    if (len > 0) feedbackError.classList.remove("visible");
  });

  // Rating Selection Buttons
  ratingButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      ratingButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      ratingValueInput.value = btn.getAttribute("data-rating");
    });
  });

  // Input Error Clearing on Type
  studentNameInput.addEventListener("input", () => {
    if (studentNameInput.value.trim()) {
      studentNameInput.classList.remove("error");
      nameError.classList.remove("visible");
    }
  });

  courseNameInput.addEventListener("input", () => {
    if (courseNameInput.value.trim()) {
      courseNameInput.classList.remove("error");
      courseError.classList.remove("visible");
    }
  });
}

// Validate Form Inputs
function validateForm(name, course, feedback) {
  let isValid = true;

  if (!name.trim()) {
    studentNameInput.classList.add("error");
    nameError.classList.add("visible");
    isValid = false;
  } else {
    studentNameInput.classList.remove("error");
    nameError.classList.remove("visible");
  }

  if (!course.trim()) {
    courseNameInput.classList.add("error");
    courseError.classList.add("visible");
    isValid = false;
  } else {
    courseNameInput.classList.remove("error");
    courseError.classList.remove("visible");
  }

  if (!feedback.trim()) {
    feedbackTextInput.classList.add("error");
    feedbackError.classList.add("visible");
    isValid = false;
  } else {
    feedbackTextInput.classList.remove("error");
    feedbackError.classList.remove("visible");
  }

  return isValid;
}

// Handle Form Submission
function handleFormSubmit(e) {
  e.preventDefault();

  const name = studentNameInput.value;
  const course = courseNameInput.value;
  const feedback = feedbackTextInput.value;
  const rating = parseInt(ratingValueInput.value) || 5;

  if (!validateForm(name, course, feedback)) {
    return;
  }

  // Create Feedback Object
  const newFeedback = {
    id: "fb-" + Date.now(),
    name: name.trim(),
    course: course.trim(),
    rating: rating,
    feedback: feedback.trim(),
    timestamp: "Just now"
  };

  // Prepend to array
  feedbacks.unshift(newFeedback);
  saveFeedbacks();

  // Reset form and render
  resetForm();
  renderFeedbacks();
  showToast("Feedback submitted successfully!");
}

// Reset Form
function resetForm() {
  feedbackForm.reset();
  ratingValueInput.value = "5";
  ratingButtons.forEach((btn, index) => {
    btn.classList.toggle("active", index === 0);
  });
  charCount.textContent = "0 / 500";

  studentNameInput.classList.remove("error");
  courseNameInput.classList.remove("error");
  feedbackTextInput.classList.remove("error");
  nameError.classList.remove("visible");
  courseError.classList.remove("visible");
  feedbackError.classList.remove("visible");
}

// Handle Clear All Feedbacks
function handleClearAll() {
  if (feedbacks.length === 0) return;
  if (confirm("Are you sure you want to clear all submitted feedback?")) {
    feedbacks = [];
    saveFeedbacks();
    renderFeedbacks();
    showToast("All feedback cleared");
  }
}

// Delete Individual Feedback
function deleteFeedback(id) {
  feedbacks = feedbacks.filter(fb => fb.id !== id);
  saveFeedbacks();
  renderFeedbacks();
  showToast("Feedback removed");
}

// Search / Filter
function handleSearch() {
  const query = searchInput.value.toLowerCase().trim();
  renderFeedbacks(query);
}

// Render Star Icons
function getStarString(rating) {
  const stars = "★".repeat(rating) + "☆".repeat(5 - rating);
  return `<span class="rating-stars">${stars}</span>`;
}

// Get User Initials for Avatar
function getInitials(name) {
  if (!name) return "ST";
  const parts = name.trim().split(" ");
  if (parts.length === 1) return parts[0].substring(0, 2).toUpperCase();
  return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
}

// Render Feedback List
function renderFeedbacks(searchQuery = "") {
  let displayList = feedbacks;

  if (searchQuery) {
    displayList = feedbacks.filter(fb => 
      fb.name.toLowerCase().includes(searchQuery) || 
      fb.course.toLowerCase().includes(searchQuery) ||
      fb.feedback.toLowerCase().includes(searchQuery)
    );
  }

  feedbackCount.textContent = feedbacks.length;

  if (displayList.length === 0) {
    feedbackList.innerHTML = "";
    emptyState.style.display = "block";
    return;
  }

  emptyState.style.display = "none";
  feedbackList.innerHTML = displayList.map(fb => `
    <article class="feedback-card" data-id="${fb.id}">
      <div class="feedback-card-top">
        <div class="user-info">
          <div class="avatar">${getInitials(fb.name)}</div>
          <div class="user-details">
            <h4>${escapeHtml(fb.name)}</h4>
            <span class="course-tag">${escapeHtml(fb.course)}</span>
          </div>
        </div>
        <div class="card-meta">
          ${getStarString(fb.rating)}
          <button class="delete-btn" onclick="deleteFeedback('${fb.id}')" title="Delete Feedback">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="3 6 5 6 21 6"></polyline>
              <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
            </svg>
          </button>
        </div>
      </div>
      <p class="feedback-body">${escapeHtml(fb.feedback)}</p>
      <span class="feedback-time">${escapeHtml(fb.timestamp)}</span>
    </article>
  `).join("");
}

// Escape HTML for XSS prevention
function escapeHtml(str) {
  if (!str) return "";
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

// Show Toast Message
function showToast(message) {
  toast.textContent = message;
  toast.classList.add("show");
  setTimeout(() => {
    toast.classList.remove("show");
  }, 2800);
}
