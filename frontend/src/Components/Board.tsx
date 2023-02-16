import React, { useState, useEffect } from 'react';
import { TaskList } from './TaskList';


interface Board {
 Name:String;
 columns: TaskList[];
}

function Board() {
  const [Boards, setBoards] = useState<Board[]>([]);

  useEffect(() => {
     async function fetchBoards() {
      const response = await fetch("127.0.0.1:8000/boards/");
      const data = await response.json();
      setBoards(data);
    }

    fetchBoards();
  }, []);

  return (
    <div></div>
  );
}

export default Board;