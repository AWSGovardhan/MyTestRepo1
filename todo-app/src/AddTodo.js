import React, { useState } from 'react';

function AddTodo({ onAdd }) {
  const [inputText, setInputText] = useState('');

  const handleInputChange = (e) => {
    setInputText(e.target.value);
  };

  const handleAddClick = () => {
    if (inputText.trim() !== '') {
      onAdd(inputText);
      setInputText('');
    }
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Add a new to-do"
        value={inputText}
        onChange={handleInputChange}
      />
      <button onClick={handleAddClick}>Add</button>
    </div>
  );
}

export default AddTodo;
