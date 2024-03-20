import React, { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { Link } from 'react-router-dom'
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'
import { ReactComponent as SaveIcon } from '../assets/save.svg'


const Note = () => {
    let params = useParams()
    let noteId = params.id

    let navigate = useNavigate()

    let [note, setNote] = useState(null)

    useEffect(() => {
        const getNote = async () => {
            if (noteId !== 'add') {
                let response = await fetch(`/notes/${noteId}`)
                let data = await response.json()
                setNote(data)
            }
        }
        getNote();
    }, [noteId])

    let submitData = async (e) => {
        e.preventDefault()

        let url = '/notes'
        let method = 'POST'

        if (params.id !== 'add') {
            url = `/notes/${params.id}`
            method = 'PUT'
        }

        let noteText = note?.text
        if (noteText !== undefined) {
            noteText = String(noteText).trim()
        }

        if (noteText === '' || noteText === undefined) {
            alert('Note cannot be empty.')
            return
        }

        await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ "text": noteText })
        })

        navigate('/')
    }

    let deleteNote = async (e) => {
        e.preventDefault()
        await fetch(`/notes/${params.id}`, { method: 'DELETE' })
        navigate('/')

    }

    return (
        <div className="note">
            <div className='note-header'>
                <h3>
                    <Link to="/">
                        <ArrowLeft />
                    </Link>
                </h3>

                {noteId !== 'add' && <button onClick={deleteNote}>Delete</button>}
            </div>

            <textarea onChange={(e) => { setNote({ ...note, 'text': e.target.value }) }} placeholder="Edit note" value={note?.text} required></textarea>

            <div onClick={submitData} className="floating-button">
                <SaveIcon />
            </div>
        </div>
    )
}

export default Note