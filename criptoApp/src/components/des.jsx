import React, { Component } from 'react'

export default class des extends Component {
    render() {
        return (
            <div>
                <div class="mb-3">
                    <label for="formFile" class="form-label">Selecciona la imagen para insertar</label>
                    <input class="form-control" type="file" id="formFile" />
                </div>
            </div>
        )
    }
}
