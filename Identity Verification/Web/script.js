document.getElementById('verificationForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('first_name', document.getElementById('firstName').value);
    formData.append('last_name', document.getElementById('lastName').value);
    formData.append('surname', document.getElementById('surname').value);
    formData.append('pan_number', document.getElementById('panNumber').value);
    formData.append('image', document.getElementById('imageUpload').files[0]);

    const response = await fetch('http://localhost:8000/verify', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    showModal(result.message);
});

function showModal(message) {
    document.getElementById('resultMessage').innerText = message;
    document.getElementById('resultModal').classList.add('show');
}

function closeModal() {
    document.getElementById('resultModal').classList.remove('show');
}