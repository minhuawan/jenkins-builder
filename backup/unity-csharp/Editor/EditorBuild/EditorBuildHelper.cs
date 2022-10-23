using System;
using System.Collections.Generic;
using System.IO;
using EditorBuild.PostProcessor;
using UnityEditor;
using UnityEditor.Callbacks;
using UnityEngine;

namespace EditorBuild
{
    public class EditorBuildHelper
    {
        private static Logger logger = Logger.GetLogger<EditorBuildHelper>();

        
        [PostProcessBuild]
        private static void PostProcessBuild(BuildTarget target, string pathToBuiltProject)
        {
            var helper = new EditorBuildHelper();
            helper.Initialize();
            helper.PostBuild(target, pathToBuiltProject);
        }

        // The method will invoked via build scripts
        public static void BuildFromCI()
        {
            var args = GetCommandLineArgs();
            foreach (var keyValuePair in args)
            {
                logger.Log($"{keyValuePair.Key}:{keyValuePair.Value}");
            }
        }

        [MenuItem("Live/Test/PostBuild")]
        private static void Test()
        {
            PostProcessBuild(BuildTarget.StandaloneWindows, @"E:\BUILDS\galaxy_studio_ff\galaxy_studio.exe");
        }

        private Config config;

        private void Initialize()
        {
            var configFile = Path.Combine(Application.dataPath, "Editor/EditorBuild/config.json");
            config = JsonUtility.FromJson<Config>(File.ReadAllText(configFile));
        }

        private void PostBuild(BuildTarget target, string pathToBuiltProject)
        {
            switch (target)
            {
                case BuildTarget.StandaloneWindows:
                case BuildTarget.StandaloneWindows64:
                    new PostProcessBuildWindows().PostProcessBuild(config, pathToBuiltProject);
                    break;
                default:
                    throw new Exception($"build post exception, unhandled target {target}");
            }
        }

        private static Dictionary<string, string> GetCommandLineArgs()
        {
            var dict = new Dictionary<string, string>();
            var args = Environment.GetCommandLineArgs();
            for (var i = 0; i < args.Length; i++)
            {
                logger.Log($"arg {i + 1}: {args[i]}");
            }

            for (var i = 0; i < args.Length; i++)
            {
                var cur = args[i];
                var nxt = i < args.Length - 1 ? args[i + 1] : "";
                if (cur.StartsWith("-"))
                {
                    if (!nxt.StartsWith("-"))
                    {
                        dict[cur] = nxt;
                        i++;
                    }
                    else
                    {
                        dict[cur] = cur;
                    }
                }
            }

            return dict;
        }
    }
}