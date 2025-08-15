// ReHearten Custom JavaScript

// Emotional state detection
const EmotionalAI = {
    emotions: ['happy', 'sad', 'angry', 'calm', 'excited', 'anxious', 'peaceful'],
    
    // Simulate emotion detection from text
    detectEmotion: function(text) {
        const emotionalKeywords = {
            happy: ['vui', 'hạnh phúc', 'tuyệt vời', 'tốt', 'yêu', 'thích'],
            sad: ['buồn', 'tệ', 'khóc', 'đau lòng', 'cô đơn'],
            angry: ['tức giận', 'bực', 'ghét', 'tức', 'điên'],
            calm: ['bình tĩnh', 'thư giãn', 'yên tâm', 'ổn định'],
            excited: ['phấn khích', 'háo hức', 'kích động', 'hào hứng'],
            anxious: ['lo lắng', 'căng thẳng', 'sợ', 'bất an'],
            peaceful: ['yên bình', 'thanh thản', 'tĩnh lặng', 'hòa bình']
        };
        
        const lowerText = text.toLowerCase();
        let maxScore = 0;
        let detectedEmotion = 'calm';
        
        for (const [emotion, keywords] of Object.entries(emotionalKeywords)) {
            let score = 0;
            keywords.forEach(keyword => {
                if (lowerText.includes(keyword)) {
                    score += 1;
                }
            });
            
            if (score > maxScore) {
                maxScore = score;
                detectedEmotion = emotion;
            }
        }
        
        return detectedEmotion;
    },
    
    // Apply emotional styling to elements
    applyEmotionalStyling: function(element, emotion) {
        element.classList.remove(...this.emotions.map(e => `emotion-${e}`));
        element.classList.add(`emotion-${emotion}`);
    },
    
    // Generate emotional response
    generateEmotionalResponse: function(userEmotion) {
        const responses = {
            happy: "Tôi rất vui khi thấy bạn hạnh phúc! 😊 Hãy chia sẻ thêm về điều gì khiến bạn vui vẻ nhé!",
            sad: "Tôi hiểu cảm giác của bạn. 🤗 Bạn có muốn chia sẻ thêm về điều gì đang làm bạn buồn không?",
            angry: "Tôi có thể cảm nhận được sự tức giận của bạn. 😔 Hãy thử hít thở sâu và kể cho tôi nghe nhé.",
            calm: "Thật tuyệt khi bạn cảm thấy bình tĩnh! 😌 Đây là trạng thái tâm lý rất tốt.",
            excited: "Wow! Tôi có thể cảm nhận được sự phấn khích của bạn! 🚀 Điều gì khiến bạn hào hứng vậy?",
            anxious: "Tôi hiểu bạn đang lo lắng. 💙 Hãy cùng tôi tìm cách để bạn cảm thấy thoải mái hơn nhé.",
            peaceful: "Cảm giác yên bình thật tuyệt vời! ☮️ Bạn có thể chia sẻ bí quyết để duy trì trạng thái này không?"
        };
        
        return responses[userEmotion] || responses.calm;
    }
};

// Heart animation effects
function addHeartEffect(element) {
    element.classList.add('heart-pulse');
    setTimeout(() => {
        element.classList.remove('heart-pulse');
    }, 2000);
}

// Initialize ReHearten features when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('ReHearten AI Platform initialized! ❤️');
    
    // Add heart effect to logo
    const logo = document.querySelector('.navbar-logo');
    if (logo) {
        logo.addEventListener('click', function() {
            addHeartEffect(this);
        });
    }
    
    // Add emotional detection to chat inputs
    const chatInputs = document.querySelectorAll('input[type="text"], textarea');
    chatInputs.forEach(input => {
        input.addEventListener('input', function() {
            const emotion = EmotionalAI.detectEmotion(this.value);
            EmotionalAI.applyEmotionalStyling(this, emotion);
        });
    });
    
    // Add welcome message
    console.log('🤖 ReHearten AI: Chào mừng bạn đến với nền tảng AI trí tuệ cảm xúc!');
});

// Export for use in other modules
window.ReHearten = {
    EmotionalAI,
    addHeartEffect
};

