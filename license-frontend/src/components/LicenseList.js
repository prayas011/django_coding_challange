import React from 'react';

const LicenseList = ({ licenses }) => {
    return (
        <div>
            <h2>Available Licenses</h2>
            <ul>
                {licenses.map(license => (
                    <li key={license.id}>{license.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default LicenseList;
