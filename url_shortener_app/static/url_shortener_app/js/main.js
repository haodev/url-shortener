// Shorten URL form
document.getElementById('shortenForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const longUrl = document.getElementById('longUrl').value.trim();
    try {
        const response = await fetch('/shorten/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: longUrl })
        });
        const data = await response.json();
        if (response.ok) {
            const shortUrl = `${data.short_url}`;
            document.getElementById('shortenResult').innerHTML = `
                <p>Short URL: <a href="${shortUrl}" target="_blank">${shortUrl}</a></p>
            `;
        } else {
            document.getElementById('shortenResult').innerHTML = `
                <p style="color: red;">Error: ${data.error}</p>
            `;
        }
    } catch (error) {
        document.getElementById('shortenResult').innerHTML = `
            <p style="color: red;">Error: ${error.message}</p>
        `;
    }
});

// Get Original URL form
document.getElementById('getOriginalForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const shortUrl = document.getElementById('shortUrl').value.trim();

    try {
        const response = await fetch(`/original/?short-url=${shortUrl}/`);
        const data = await response.json();

        if (response.ok) {
            document.getElementById('getOriginalResult').innerHTML = `
                <p>Original URL: <a href="${data.original_url}" target="_blank">${data.original_url}</a></p>
            `;
        } else {
            document.getElementById('getOriginalResult').innerHTML = `
                <p style="color: red;">Error: ${data.error}</p>
            `;
        }
    } catch (error) {
        document.getElementById('getOriginalResult').innerHTML = `
            <p style="color: red;">Error: ${error.message}</p>
        `;
    }
});

// Redirect form
document.getElementById('redirectForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const shortUrl = document.getElementById('redirectShortUrl').value.trim();
    try {
        // Find the original url
        const response = await fetch(`/original/?short-url=${shortUrl}/`);
        const data = await response.json();

        console.log(shortUrl)
        if (response.ok) {
            // If successful, redirect to the original URL
            window.location.href = `/redirect/?short-url=${shortUrl}`;
        } else {
            // Show error message if URL not found
            document.getElementById('redirectResult').innerHTML = `
                <p style="color: red;">Error: ${data.error}</p>
            `;
        }
    } catch (error) {
        document.getElementById('redirectResult').innerHTML = `
            <p style="color: red;">Error: Invalid URL or server error</p>
        `;
    }
});
