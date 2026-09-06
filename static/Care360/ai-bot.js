// ==========================================
// CARE360 AI ASSISTANT
// ==========================================


// GET HTML ELEMENTS
const aiButton = document.getElementById("ai-button");
const aiChat = document.getElementById("ai-chat");
const aiClose = document.getElementById("ai-close");

const aiInput = document.getElementById("ai-input");
const aiSend = document.getElementById("ai-send");

const aiMessages = document.getElementById("ai-messages");


// ==========================================
// OPEN CHAT
// ==========================================

aiButton.addEventListener("click", () => {

    aiChat.classList.add("active");

    // Automatically focus input
    setTimeout(() => {
        aiInput.focus();
    }, 200);

});


// ==========================================
// CLOSE CHAT
// ==========================================

aiClose.addEventListener("click", () => {

    aiChat.classList.remove("active");

});


// ==========================================
// SEND BUTTON
// ==========================================

aiSend.addEventListener("click", sendMessage);


// ==========================================
// ENTER KEY
// ==========================================

aiInput.addEventListener("keydown", (event) => {

    if (event.key === "Enter") {

        event.preventDefault();

        sendMessage();

    }

});


// ==========================================
// SEND MESSAGE
// ==========================================

async function sendMessage() {

    const message = aiInput.value.trim();


    // Don't send empty messages
    if (!message) {
        return;
    }


    // --------------------------------------
    // SHOW USER MESSAGE
    // --------------------------------------

    addMessage(message, "user");


    // Clear input
    aiInput.value = "";


    // --------------------------------------
    // DISABLE INPUT WHILE AI THINKS
    // --------------------------------------

    aiInput.disabled = true;
    aiSend.disabled = true;


    // --------------------------------------
    // SHOW THINKING MESSAGE
    // --------------------------------------

    const loading = addMessage(
        "Thinking...",
        "bot"
    );


    try {

        // ----------------------------------
        // SEND REQUEST TO DJANGO
        // ----------------------------------

        const response = await fetch("/api/chat/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        // ----------------------------------
        // CHECK SERVER RESPONSE
        // ----------------------------------

        if (!response.ok) {

            throw new Error(
                `Server error: ${response.status}`
            );

        }


        const data = await response.json();


        // ----------------------------------
        // REMOVE THINKING MESSAGE
        // ----------------------------------

        loading.remove();


        // ----------------------------------
        // SHOW AI RESPONSE
        // ----------------------------------

        if (data.reply) {

            addMessage(
                data.reply,
                "bot"
            );

        } else {

            addMessage(
                "I'm sorry, I couldn't generate a response.",
                "bot"
            );

        }


    } catch (error) {

        // ----------------------------------
        // REMOVE THINKING MESSAGE
        // ----------------------------------

        loading.remove();


        // ----------------------------------
        // ERROR MESSAGE
        // ----------------------------------

        addMessage(
            "⚠️ I'm having trouble connecting to the AI right now. Please try again.",
            "bot"
        );


        console.error(
            "Care360 AI Error:",
            error
        );

    }


    // --------------------------------------
    // ENABLE INPUT AGAIN
    // --------------------------------------

    aiInput.disabled = false;
    aiSend.disabled = false;

    aiInput.focus();

}


// ==========================================
// ADD MESSAGE
// ==========================================

function addMessage(text, type) {

    const messageDiv =
        document.createElement("div");


    // --------------------------------------
    // MESSAGE TYPE
    // --------------------------------------

    if (type === "user") {

        messageDiv.classList.add(
            "user-message"
        );

    } else {

        messageDiv.classList.add(
            "bot-message"
        );

    }


    // --------------------------------------
    // MESSAGE TEXT
    // --------------------------------------

    messageDiv.textContent = text;


    // --------------------------------------
    // ADD TO CHAT
    // --------------------------------------

    aiMessages.appendChild(
        messageDiv
    );


    // --------------------------------------
    // AUTO SCROLL
    // --------------------------------------

    aiMessages.scrollTop =
        aiMessages.scrollHeight;


    return messageDiv;

}
