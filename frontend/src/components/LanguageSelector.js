import React from 'react';
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material';

function LanguageSelector({ onLanguageChange }) {
    const handleLanguageChange = (e) => {
        onLanguageChange(e.target.value);
    };

    return (
        <FormControl fullWidth variant="outlined">
            <InputLabel id="language-label">Select Language</InputLabel>
            <Select
                labelId="language-label"
                id="language"
                label="Select Language"
                onChange={handleLanguageChange}
                defaultValue="en"
            >
                <MenuItem value="en">English</MenuItem>
                <MenuItem value="es">Spanish</MenuItem>
                <MenuItem value="fr">French</MenuItem>
                <MenuItem value="de">German</MenuItem>
                <MenuItem value="zh-cn">Chinese (Simplified)</MenuItem>
                {/* Add more languages as needed */}
            </Select>
        </FormControl>
    );
}

export default LanguageSelector;
