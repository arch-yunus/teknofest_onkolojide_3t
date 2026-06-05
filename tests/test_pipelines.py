import pytest
import numpy as np
from src.utils.rano_criteria import evaluate_rano_response
from src.utils.surgical_planner import calculate_surgical_margins
from src.utils.algology_monitor import predict_pain_intensity

def test_rano_response():
    # Test Stable Disease (SD)
    result = evaluate_rano_response(100.0, 110.0)
    assert result['response_category'] == 'SD'
    
    # Test Partial Response (PR)
    result = evaluate_rano_response(100.0, 40.0)
    assert result['response_category'] == 'PR'
    
    # Test Progressive Disease (PD)
    result = evaluate_rano_response(100.0, 130.0)
    assert result['response_category'] == 'PD'

def test_surgical_margins():
    # Mock segmentation mask
    mock_mask = np.zeros((10, 10, 10))
    mock_mask[4:6, 4:6, 4:6] = 1 # Tumor region
    
    result = calculate_surgical_margins(mock_mask, margin_mm=5.0)
    assert 'tumor_volume_ml' in result
    assert 'safety_score' in result

def test_pain_intensity():
    result = predict_pain_intensity(40.0, 70.0, 5)
    assert 'predicted_vas' in result
    assert 'pain_level' in result
    assert result['predicted_vas'] >= 0 and result['predicted_vas'] <= 10
