import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import axios from 'axios';
import LanguageSelector from '../components/LanguageSelector';
import ChatMessage from '../components/ChatMessage';
import { Box, TextField, Button, Typography } from '@mui/material';

const socket = io('http://localhost:5000');

function ChatPage() {
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState('');
    const [language, setLanguage] = useState('en');

    useEffect(() => {
        socket.on('receiveMessage', (msg) => {
            setMessages((prev) => [...prev, msg]);
        });

        return () => socket.off('receiveMessage');
    }, []);

    const handleLanguageChange = (selectedLanguage) => {
        setLanguage(selectedLanguage);
    };

    const sendMessage = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(
                `${process.env.REACT_APP_API_URL}/chat/message`,
                { message, language }
            );
            socket.emit('sendMessage', response.data.ai_response);
            setMessages((prev) => [...prev, { message, ai_response: response.data.ai_response }]);
            setMessage('');
        } catch (err) {
            console.error(err);
        }
    };

    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <Typography variant="h4" component="h1" gutterBottom>
                Chat
            </Typography>
            <LanguageSelector onLanguageChange={handleLanguageChange} />
            <Box sx={{ width: '100%', mt: 2 }}>
                {messages.map((msg, index) => (
                    <ChatMessage key={index} message={msg.message} aiResponse={msg.ai_response} />
                ))}
            </Box>
            <Box component="form" onSubmit={sendMessage} sx={{ display: 'flex', width: '100%', mt: 2 }}>
                <TextField
                    fullWidth
                    label="Type a message"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                />
                <Button
                    type="submit"
                    variant="contained"
                    sx={{ ml: 2 }}
                >
                    Send
                </Button>
            </Box>
        </Box>
    );
}

export default ChatPage;
