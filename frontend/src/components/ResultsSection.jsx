import { useEffect, useState } from 'react'

export default function ResultsSection({
  results,
  preview,
  onReset,
  onDownload,
  formatClassName
}) {
  const [confidenceWidth, setConfidenceWidth] = useState(0)
  const [top5Widths, setTop5Widths] = useState([])

  useEffect(() => {
    setTimeout(() => {
      setConfidenceWidth(parseFloat(results.confidence))
    }, 100)

    const widths = results.top5.map((_, index) => {
      const confidence = parseFloat(results.top5[index].confidence)
      return confidence
    })

    setTimeout(() => {
      setTop5Widths(widths)
    }, 100)
  }, [results])

  return (
    <div className="results-section">
      <div className="results-card">
        {preview && (
          <div className="results-preview">
            <img src={preview} alt="Analyzed" />
          </div>
        )}

        <div className="main-result">
          <div className="result-header">
            <h2>Hasil Prediksi</h2>
            <i className="fas fa-check-circle success-icon"></i>
          </div>

          <div className="predicted-class-card">
            <p className="label">Diagnosis:</p>
            <h3>{formatClassName(results.predicted_class)}</h3>
            <div className="confidence-bar">
              <div
                className="confidence-fill"
                style={{ width: `${confidenceWidth}%` }}
              ></div>
            </div>
            <p className="confidence-text">
              Confidence: <span>{parseFloat(results.confidence).toFixed(2)}</span>%
            </p>
          </div>
        </div>

        <div className="top-predictions">
          <h3>
            <i className="fas fa-list-check"></i> Top 5 Prediksi
          </h3>
          <div className="predictions-list">
            {results.top5.map((pred, index) => (
              <div key={index} className="prediction-item">
                <div className="prediction-rank">{index + 1}</div>
                <div className="prediction-class">
                  {formatClassName(pred.class)}
                </div>
                <div className="prediction-confidence">
                  <div className="prediction-confidence-bar">
                    <div
                      className="prediction-confidence-fill"
                      style={{
                        width: `${top5Widths[index] ? parseFloat(top5Widths[index]) : 0}%`
                      }}
                    ></div>
                  </div>
                  <div className="prediction-value">
                    {parseFloat(pred.confidence).toFixed(2)}%
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="action-buttons">
          <button className="btn-reset" onClick={onReset}>
            <i className="fas fa-redo"></i> Analisis Gambar Lain
          </button>
          <button className="btn-download" onClick={onDownload}>
            <i className="fas fa-download"></i> Download Hasil
          </button>
        </div>
      </div>
    </div>
  )
}
