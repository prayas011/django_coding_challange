import React, { useState } from 'react';

const LicenseForm = ({ onAdd }) => {
    const [name, setName] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onAdd({ name });
        setName('');
    };

    return (
        <div>
            <h2>Add New License</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={name}
                    onChange={e => setName(e.target.value)}
                    placeholder="License Name"
                />
                <button type="submit">Add</button>
            </form>
        </div>
    );
}

export default LicenseForm;
