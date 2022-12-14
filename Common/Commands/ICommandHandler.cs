/*
 * QUANTCONNECT.COM - Democratizing Finance, Empowering Individuals.
 * Lean Algorithmic Trading Engine v2.0. Copyright 2014 QuantConnect Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

using System;
using QuantConnect.Packets;
using QuantConnect.Interfaces;
using System.Collections.Generic;

namespace QuantConnect.Commands
{
    /// <summary>
    /// Represents a command queue for the algorithm. This is an entry point
    /// for external messages to act upon the running algorithm instance.
    /// </summary>
    public interface ICommandHandler : IDisposable
    {
        /// <summary>
        /// Initializes this command queue for the specified job
        /// </summary>
        /// <param name="job">The job that defines what queue to bind to</param>
        /// <param name="algorithm">The algorithm instance</param>
        void Initialize(AlgorithmNodePacket job, IAlgorithm algorithm);

        /// <summary>
        /// Process any commands in the queue
        /// </summary>
        /// <returns>The command result packet of each command executed if any</returns>
        IEnumerable<CommandResultPacket> ProcessCommands();
    }
}
