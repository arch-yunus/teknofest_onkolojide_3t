import pytest
from src.main import GlioSightEngine

def test_engine_initialization():
    engine = GlioSightEngine()
    assert engine.seg_pipeline is not None
    assert engine.surv_pipeline is not None
    assert engine.radio_pipeline is not None
    assert engine.xai_pipeline is not None
    assert engine.pathology_emulator is not None
    assert engine.precision_pipeline is not None
