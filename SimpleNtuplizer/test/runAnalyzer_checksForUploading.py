import FWCore.ParameterSet.Config as cms

from Configuration.AlCa.GlobalTag import GlobalTag

process = cms.Process("EenTest")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )

process.load('Configuration/EventContent/EventContent_cff')
process.load("Configuration.StandardSequences.Services_cff")
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("RecoEcal.EgammaCoreTools.EcalNextToDeadChannelESProducer_cff")

#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc'   , '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '100X_upgrade2018_realistic_Fromv10ExtZeroMaterial_v1', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, '105X_mc2017_realistic_v5', '')

process.GlobalTag = GlobalTag(process.GlobalTag, '105X_upgrade2018_realistic_v4', '')
###replace here
process.GlobalTag.toGet.extend( cms.VPSet(
#process.GlobalTag.toGet.replace( cms.VPSet(
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EB_ZS_mean_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EB_ZS_mean_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EB_ZS_mean_25ns.db')
            ),
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EB_Full_ptbin1_mean_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EB_Full_ptbin1_mean_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EB_Full_ptbin1_mean_25ns.db')
            ),
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EB_Full_ptbin2_mean_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EB_Full_ptbin2_mean_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EB_Full_ptbin2_mean_25ns.db')
            ),

        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EB_Full_ptbin3_mean_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EB_Full_ptbin3_mean_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EB_Full_ptbin3_mean_25ns.db')
            ),

        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EB_ZS_sigma_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EB_ZS_sigma_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EB_ZS_sigma_25ns.db')
            ),
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EB_Full_ptbin1_sigma_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EB_Full_ptbin1_sigma_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EB_Full_ptbin1_sigma_25ns.db')
            ),
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EB_Full_ptbin2_sigma_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EB_Full_ptbin2_sigma_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EB_Full_ptbin2_sigma_25ns.db')
            ),
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EB_Full_ptbin3_sigma_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EB_Full_ptbin3_sigma_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EB_Full_ptbin3_sigma_25ns.db')
            ),
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EE_ZS_mean_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EE_ZS_mean_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EE_ZS_mean_25ns.db')
            ),
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EE_Full_ptbin1_mean_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EE_Full_ptbin1_mean_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EE_Full_ptbin1_mean_25ns.db')
            ),
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EE_Full_ptbin2_mean_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EE_Full_ptbin2_mean_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EE_Full_ptbin2_mean_25ns.db')
            ),


        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EE_Full_ptbin3_mean_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EE_Full_ptbin3_mean_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EE_Full_ptbin3_mean_25ns.db')
            ),


        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EE_ZS_sigma_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EE_ZS_sigma_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EE_ZS_sigma_25ns.db')
            ),
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EE_Full_ptbin1_sigma_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EE_Full_ptbin1_sigma_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EE_Full_ptbin1_sigma_25ns.db')
            ),
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EE_Full_ptbin2_sigma_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EE_Full_ptbin2_sigma_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EE_Full_ptbin2_sigma_25ns.db')
            ),
        cms.PSet(
            record = cms.string('GBRDWrapperRcd'),
            tag = cms.string('ecalPFClusterCor2018ULV2_EE_Full_ptbin3_sigma_25ns'),
            label = cms.untracked.string('ecalPFClusterCor2017V2_EE_Full_ptbin3_sigma_25ns'),
            connect = cms.string('sqlite_file:ecalPFClusterCor2018ULV2_EE_Full_ptbin3_sigma_25ns.db')
            ),
        ))


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )
process.options = cms.untracked.PSet( allowUnscheduled = cms.untracked.bool(True) )

readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 

#readFiles.extend([
#        'file:0220DA0C-648C-E611-A9AA-0CC47A78A2F6.root'
        #'/store/data/Run2016B/SingleElectron/AOD/23Sep2016-v2/80000/0220DA0C-648C-E611-A9AA-0CC47A78A2F6.root',
        #'/store/mc/RunIISpring16DR80/DoubleElectron_FlatPt-300To6500/AODSIM/PUFlat0to50_80X_mcRun2_asymptotic_2016_v3-v1/00000/0A240112-4406-E611-9A29-20CF3027A5CE.root',
        #'/store/mc/RunIISpring16DR80/DoubleElectron_FlatPt-1To300/AODSIM/PUFlat0to50_80X_mcRun2_asymptotic_2016_v3-v1/00000/0054673A-0306-E611-A949-0025905C2CD0.root'
        #'/store/user/rcoelhol/GluGluHToGG_M-125_13TeV_powheg_pythia8/crab_HggClusters/170327_193908/0000/skimEGMobjects_fromRAW_1.root'
        #'/store/user/rcoelhol/GluGluHToGG_M-125_13TeV_powheg_pythia8/crab_HggClusters_v2/170331_114027/0000/skimEGMobjects_fromRAW_101.root',
#])

process.source = cms.Source(
    "PoolSource",
    #fileNames = readFiles,
    #secondaryFileNames = secFiles
    fileNames = cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/PFClusterCalibration/debug_2018UL/skimEGMobjects_fromRAW_newCorr.root')
    )

#for file in open("fileslist_PU_0p01TO5.list").readlines():
#for file in open("#FILE.LIST").readlines():
#for file in open("tmp.list").readlines():
#    process.source.fileNames.append(file.strip())
    
########################################
# Define the analyzer
########################################

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("/eos/cms/store/group/phys_egamma/PFClusterCalibration/debug_2018UL/tree_newCorr.root"),
                                   #fileName = cms.string("root://eoscms.cern.ch//eos/cms/store/group/phys_egamma/PFClusteRegressionTrees/pfCluster_PU_0p01To5.root"),
                                   #fileName = cms.string("/tmp/shilpi/#OUT.ROOT"),
                                   closeFileFast = cms.untracked.bool(True)
                                   )


process.een_analyzer = cms.EDAnalyzer(
    'SimpleNtuplizer',
    vertices            = cms.InputTag("offlinePrimaryVertices", ""),
    electrons           = cms.InputTag("gedGsfElectrons", ""),
    photons             = cms.InputTag("gedPhotons", ""),
    superClustersEB     = cms.InputTag("particleFlowSuperClusterECAL", "particleFlowSuperClusterECALBarrel"),
    superClustersEE     = cms.InputTag("particleFlowSuperClusterECAL", "particleFlowSuperClusterECALEndcapWithPreshower"),
    pfLabel             = cms.InputTag("particleFlowClusterECALMatchedToPhotons"),
    rho                 = cms.InputTag("fixedGridRhoFastjetAll", ""),
    genparticles        = cms.InputTag("genParticles", ""),
    PUInfoInputTag      = cms.InputTag("addPileupInfo", ""),
    genEvtInfoInputTag  = cms.InputTag("generator", ""),
    ecalrechitsEB       = cms.InputTag("reducedEcalRecHitsEB"),
    ecalrechitsEE       = cms.InputTag("reducedEcalRecHitsEE"),
    ebSrFlagCollection  = cms.InputTag("ecalDigis"),
    eeSrFlagCollection  = cms.InputTag("ecalDigis"),
    ps1Label             = cms.InputTag("particleFlowClusterECALMatchedToPhotons","PS1"),
    ps2Label             = cms.InputTag("particleFlowClusterECALMatchedToPhotons", "PS2"),
    
    doElectronTree      = cms.bool(False),
    doPhotonTree        = cms.bool(False),
    doSuperClusterTree  = cms.bool(False),
    doPFClusterTree     = cms.bool(True),
    doVertex            = cms.bool(True),
    doTagAndProbe       = cms.bool(False),
    saveUnmatched       = cms.bool(False),
    isData              = cms.bool(False)

    )
    
process.p = cms.Path(process.een_analyzer)
