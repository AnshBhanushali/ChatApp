import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

function ChatMessage({ message, aiResponse }) {
    return (
        <Card variant="outlined" sx={{ mb: 2 }}>
            <CardContent>
                <Typography variant="body1"><strong>You:</strong> {message}</Typography>
                <Typography variant="body2" color="textSecondary"><strong>AI:</strong> {aiResponse}</Typography>
            </CardContent>
        </Card>
    );
}

export default ChatMessage;
