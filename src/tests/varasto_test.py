import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_varaston_tilavuus_ei_negatiivinen(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_varaston_saldo_ei_negatiivinen(self):
        self.varasto = Varasto(10, alku_saldo=-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_varaston_saldo_ei_yli_tilavuus(self):
        self.varasto = Varasto(10, alku_saldo=20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_liian_suuri_lisays_ei_ylitä_tilavuutta(self):
        self.varasto.lisaa_varastoon(-8)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_maara_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_yli_saldon_palauttaa_kaiken(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_merkkijono_on_oikea(self):
        self.varasto.lisaa_varastoon(8)
        self.assertEqual(str(self.varasto), "saldo = 8, vielä tilaa 2" )