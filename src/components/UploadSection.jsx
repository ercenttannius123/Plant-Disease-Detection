import { useRef } from 'react'

export default function UploadSection({
  preview,
  onFileSelect,
  onRemoveFile,
  onPredict,
  selectedFile
}) {
  const fileInputRef = useRef(null)
  const dropZoneRef = useRef(null)

  const handleDragOver = (e) => {
    e.preventDefault()
    dropZoneRef.current?.classList.add('dragover')
  }

  const handleDragLeave = () => {
    dropZoneRef.current?.classList.remove('dragover')
  }

  const handleDrop = (e) => {
    e.preventDefault()
    dropZoneRef.current?.classList.remove('dragover')

    const files = e.dataTransfer.files
    if (files.length > 0) {
      onFileSelect(files[0])
    }
  }

  const handleFileInputChange = (e) => {
    if (e.target.files[0]) {
      onFileSelect(e.target.files[0])
    }
  }

  return (
    <div className="upload-section">
      <div className="upload-card">
        {!preview && (
          <>
            <div
              ref={dropZoneRef}
              className="upload-area"
              onDragOver={handleDragOver}
              onDragLeave={handleDragLeave}
              onDrop={handleDrop}
              onClick={() => fileInputRef.current?.click()}
            >
              <i className="fas fa-cloud-upload-alt"></i>
              <h2>Upload Gambar Tanaman</h2>
              <p>Drag & drop gambar atau klik untuk memilih</p>
            </div>
            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              onChange={handleFileInputChange}
              style={{ display: 'none' }}
            />
            <button
              className="btn-browse"
              onClick={() => fileInputRef.current?.click()}
            >
              <i className="fas fa-folder-open"></i> Pilih File
            </button>
          </>
        )}

        {preview && (
          <>
            <div className="image-preview">
              <div className="preview-container">
                <img src={preview} alt="Preview" />
                <button className="btn-remove" onClick={onRemoveFile}>
                  <i className="fas fa-times"></i>
                </button>
              </div>
            </div>

            <button
              className="btn-upload"
              onClick={onPredict}
              disabled={!selectedFile}
            >
              <i className="fas fa-paper-plane"></i> Analisis Sekarang
            </button>
          </>
        )}
      </div>
    </div>
  )
}
