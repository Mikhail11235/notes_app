import React from 'react'
import { Link } from 'react-router-dom'

let getTimestamp = (note) => {
    return new Date(note.updated_at).toLocaleString()
}

let trimmedContent = (note) => {
    let content = note.text
    if (content.length > 45) {
        return content.slice(0, 45) + '...'
    } else {
        return content
    }
}

const ListItem = ({ note }) => {
    return (
        <Link to={`/${note.id}`}>
            <div className="notes-list-item">
                <h3>{trimmedContent(note)}</h3>
                <p><span>{getTimestamp(note)}</span></p>
            </div>
        </Link>
    )
}

export default ListItem