import React, { useState, useEffect } from 'react';

function EmailLogs() {
    const [logs, setLogs] = useState([]);

    useEffect(() => {
        fetch("http://localhost:8000/api/email-logs/") 
        .then(response => response.json())
        .then(data => setLogs(data))
        .catch(error => console.error("Error fetching email logs:", error));
    }, []);

    return (
        <div>
            <h2>Email Logs</h2>
            <ul>
                {logs.map(log => (
                    <li key={log.id}>
                        {/* Adjust the fields based on your model */}
                        {log.email_subject}: {log.sent_at}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default EmailLogs;
