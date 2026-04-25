export default function ErrorSection({ error, onRetry }) {
  return (
    <div className="error-section">
      <div className="error-card">
        <i className="fas fa-exclamation-triangle"></i>
        <h3>Terjadi Kesalahan</h3>
        <p>{error}</p>
        <button className="btn-retry" onClick={onRetry}>
          <i className="fas fa-redo"></i> Coba Lagi
        </button>
      </div>
    </div>
  )
}
